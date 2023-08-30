# this file is called to_csv.py
import mido
from mido import MidiFile, MidiTrack, MetaMessage
import csv
import argparse

def midi_to_csv(midi_file_path, csv_file_path):
    mid = MidiFile(midi_file_path)

    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = ['start_time_s', 'end_time_s', 'pitch_midi', 'velocity', 'pitch_bend']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        current_time_s = 0
        note_on_events = {}

        for track in mid.tracks:
            for msg in track:
                if msg.type == "set_tempo":
                    # Extract tempo and save it to a file
                    with open(f"{midi_file_path}.tempo", 'w') as tempo_file:
                        tempo_file.write(str(msg.tempo))

        for msg in mid.play():
            current_time_s += msg.time

            if msg.type == 'note_on' and msg.velocity > 0:
                note_on_events[msg.note] = (current_time_s, msg.velocity)
            elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
                start_time, velocity = note_on_events.pop(msg.note, (None, 0))
                if start_time is not None:
                    writer.writerow({
                        'start_time_s': start_time,
                        'end_time_s': current_time_s,
                        'pitch_midi': msg.note,
                        'velocity': velocity,  # Using stored velocity
                        'pitch_bend': 0  # assuming no pitch bend
                    })
            elif msg.type == 'pitchwheel':
                # If you need to handle pitch bends in the context of the ongoing notes, this part will need more logic.
                pass

    print(f"Transcribed {midi_file_path} to {csv_file_path}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Transcribe MIDI file to CSV.')
    parser.add_argument('-m', '--midi_file_path', type=str, required=True, help='Path to the input MIDI file.')
    parser.add_argument('-c', '--csv_file_path', type=str, help='Path to the output CSV file.')

    args = parser.parse_args()

    csv_file_path = None
    if args.csv_file_path==None:
        csv_file_path = args.midi_file_path + ".csv"
    else:
        csv_file_path = args.csv_file_path

    midi_to_csv(args.midi_file_path, csv_file_path)

