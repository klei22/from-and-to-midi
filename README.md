# MIDI to CSV and CSV to MIDI Conversion

This repository contains Python scripts for converting MIDI files to CSV format
and CSV files back to MIDI format. It utilizes the `mido` library for MIDI file
handling.

## Requirements

To run the scripts, you need to have the following dependencies installed:

- mido==1.3.0
- csv (built-in module)

You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

### MIDI to CSV Conversion

To convert a MIDI file to CSV format, use the `to_csv.py` script.

Provide the path to the input MIDI file and the desired output CSV file as
arguments.

For example:
```bash
python to_csv.py -m input.mid -c output.csv
```
If no `-c` is specified, then the output file will be named `input.mid.csv`.

### CSV to MIDI Conversion

To convert a CSV file back to MIDI format, use the `to_midi.py` script.

Provide the path to the input CSV file and the desired output MIDI file as arguments.

For example:
```bash
python to_midi.py -c input.csv -m output.mid
```

If no `-m` is specified, then the output file will be named `input.csv.mid`.

You can also specify an optional tempo file using the `-t` argument.

Make sure to adjust the script if you have specific MIDI settings or pitch bend data.

## License

This project is licensed under the Apache-2.0 License. See the [LICENSE](LICENSE) file for details.
