![RavenEye Logo](cover.png)

## Installation
1. Clone Repo
`
git clone https://github.com/diogo-beijinha/raveneye/
`
2. Get requirements
`
pip install -r requirements.txt
`

## Usage

- Scan all ports
`
python raveneye.py -i <ip>
`
- Scan certain range of ports
`
python raveneye.py -i <ip> -p <range_start-range_end>
`

Future Implementations:
- Allow user to save results to a file
- Check if scanned SMB port allows Anonymous connections
