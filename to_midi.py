import mido
from mido import MidiFile, MidiTrack, Message
from mido import MetaMessage
import csv

def csv_to_midi(csv_file_path, midi_file_path):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    track.append(MetaMessage('set_tempo', tempo=1000000))
    events = []

    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            start_time_s = float(row['start_time_s'])
            end_time_s = float(row['end_time_s'])
            pitch_midi = int(row['pitch_midi'])
            velocity = int(row['velocity'])
            
            events.append(('note_on', start_time_s, pitch_midi, velocity))
            events.append(('note_off', end_time_s, pitch_midi, velocity))
            
    # Sort events by timestamp
    events.sort(key=lambda x: x[1])

    prev_time_s = 0
    for event in events:
        event_type, time_s, pitch_midi, velocity = event

        # Convert time from seconds to ticks
        delta_ticks = int((time_s - prev_time_s) * mid.ticks_per_beat)
        
        if event_type == 'note_on':
            track.append(Message('note_on', note=pitch_midi, velocity=velocity, time=delta_ticks))
        elif event_type == 'note_off':
            track.append(Message('note_off', note=pitch_midi, velocity=velocity, time=delta_ticks))
            
        prev_time_s = time_s

    mid.save(midi_file_path)
    print(f"Converted {csv_file_path} to {midi_file_path}")

if __name__ == "__main__":
    csv_to_midi('output.csv', 'from_csv.mid')

