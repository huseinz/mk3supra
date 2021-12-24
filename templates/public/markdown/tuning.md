The following is for my 7M-GTE running the ECUMasters EMU Black ECU.

## Docs
- [EMU Black Training Manual](https://drive.google.com/file/d/1-_NAlyTh8-dYGTJImPhoPie9wzJ2CXCW/view)
- [EMU Black Reference Manual](https://drive.google.com/file/d/1EdAFo1TTJCEsH4Wx4Oo1ipDlBnCn-KV1/view?usp=sharing)
- Firmware version I am using: [2.126 (test version)](https://www.ecumaster.com/files/EMU_BLACK/EMUBlackSetup_2_136.exe)

## Pinout

### Black 39-pin Connector

|Pin    |Desc         |Note    |Pin    |Desc         |Note    |Pin    |Desc         |Note    |
|---    |---------    |----    |---    |---------    |----    |---    |---------    |----    |
|  1    |IC &nbsp;#5  |        | 13    |IC &nbsp;#4  |        | 27    |P &nbsp; GND |✅      |
|  2    |EGT #1       |        | 15    |EGT #2       |        | 28    |ECU GND      |✅      |
|  3    |KS &nbsp;#1  |✅      | 16    |KS &nbsp;#2  |✅      | 29    |S &nbsp; GND |✅KS 1&2|
|  4    |AI &nbsp;#2  |        | 17    |AI &nbsp;#3  |        | 30    |AI &nbsp;#4  |        |
|  5    |CLT          |✅      | 18    |TPS          |✅      | 31    |AI &nbsp;#1  |        |
|  6    |WBO Vs       |✅      | 19    |WBO Ip       |✅      | 32    |IAT          |✅      |
|  7    |CAM #2       |        | 20    |VSS         |✅Cluster| 33    |WBO VGND     |✅      |
|  8    |Pri. Trigger |✅      | 21    |CAM #1       |✅      | 34    |+5V          |✅TPS   |
|  9    |Flex Fuel    |        | 22    |WBO Rcal     |✅      | 35    |AI &nbsp;#5  |✅Oil P |
| 10    |SW &nbsp;#1  |✅Clutch| 23    |SW &nbsp;#2  |        | 36    |SW &nbsp;#3  |✅Sport |
| 11    |TXD          |        | 24    |RXD          |        | 37    |AI &nbsp;#6  |✅Oil T |
| 12    |CAN H        |✅      | 25    |CAN L        |✅      | 38    |S &nbsp; GND |✅Triggers|
| 13    |Batt. 12V    |✅      | 26    |+5V          |✅      | 39    |S &nbsp; GND |✅Others|

### Gray 24-pin Connector
|Pin    |Desc         |Note    |Pin    |Desc         |Note    |Pin    |Desc         |Note    |
|---    |---------    |----    |---    |---------    |----    |---    |---------    |----    |
|  1    |IC &nbsp;#6  |        |  9    |IC &nbsp;#3  |✅      | 17    |P &nbsp; GND |✅      |
|  2    |HB &nbsp;#1A |        | 10    |HB &nbsp;#1B |        | 18    |IGN 12V      |✅      |
|  3    |HB &nbsp;#1B |        | 11    |HB &nbsp;#2B |        | 19    |WBO Heater   |✅      |
|  4    |AUX #6       |        | 12    |AUX #5     |✅FP Relay| 20    |AUX #4       |✅Tach  |
|  5    |AUX #3      |✅PWM Fan| 13    |AUX #2     |✅PWM Idle| 21    |AUX #1       |✅PWM Boost|
|  6    |INJ #4       |✅      | 14    |INJ #5       |✅      | 22    |INJ #6       |✅      |
|  7    |INJ #1       |✅      | 15    |INJ #2       |✅      | 23    |INJ #3       |✅      |
|  8    |IC &nbsp;#1  |✅      | 16    |IC &nbsp;#2  |✅      | 24    |P &nbsp; GND |✅      |

## Specs
*If something is not mentioned here, assume it is stock*
### Engine, Electrical
- ***Sensors*** 
	- ***Trigger***
		- **B8** Primary Trigger:
		- **B21** Camsync In #1:
	- **Knock**
	- ***Oxygen***
		- Bosch LSU 4.9 for ECU input
		- Bosch LSU 4.2 for AEM A/F gauge
	- ***Pressure***
		- AI#, LDM 0-100psi: oil pressure, mounted at the '7M' inscription port
		- AI#, LDM 0-100psi: fuel pressure, mounted in AFPR gauge port
	- ***Temperature***
		- **B5** CLT, 89+ Toyota: coolant temperature, stock sensor port
		- **B32** IAT, Bosch 0280130085: intake air temperature, mounted in 3000 pipe
		- **B37** AI#6, AEM 30-2012: oil temperature, placed pre-filter at oil pump outlet
- ***Ignition***
	- **Coils**: IS300 2JZ-GE waste-spark coils using EMU Black internal igniter. ~3ms dwell
- ***Fuel***
	- Walbro 255, 12V mod. -6AN feed and return
	- DeatschWerks DWR1000i adjustable fuel pressure regulator, 50psi @ atmospheric
	- Bosch 550cc low-Z injectors from Driftmotion
	- Using 91-95 Acura Legend 6-channel fuel injector resistor to support sequential injection with low-Z injectors. I should upgrade to larger high-Z injectors eventually so I don't need this resistor.
- ***Boost***
	- AUX5: MAC-type solenoid, AEM 30-2400
- ***Idle***
	- Bosch 2-wire PWM valve 0280140551, plumbed between charge pipe and intake manifold
- ***Fan***
	- 2004 Dodge Stratus fans, made by Bosch
	- AUX : Ford RR28 PWM fan controllers, one per fan

### Engine, Mechanical
- ***Cylinder Head***
	- **Springs**: BC
	- **Head Gasket**: Cometic
- ***Cylinder Block***
	- ARP main studs
- ***Rotating Assembly***
	- **Pistons**: Wiseco 84.5mm
	- **Rods**: Eagle
	- **Bearings**: Taiho, standard size
	- **Harmonic Dampener**: ATI
	- **Clutch**: ACT 3000608 Street Sprung Full-face disc
	- **Driveshaft**: Shaftmasters, aluminum
- ***Turbocharger***
	- Albert Meade 57-trim CT26 (more specs to come)
	- -4AN oil feed and coolant lines
	- -10AN oil drain
- ***Intake***
	- **Piping**: 2.5"
	- **BOV**: some HKS SSQV clone with a big cone on it
	- **Intercooler**: Sparco clone
- ***Exhaust***
	- **Downpipe**: Driftmotion CT-26 bellmouth downpipe
	- **Piping**: RS-R 3"
	- **Resonator**: Vibrant Ultra-Quiet
- ***Lubrication***
	- Driftmotion billet remote-oil filter kit with -10AN lines
	- Setrab thermostatic sandwich plate
	- Mishimoto 11-row oil cooler clone
- ***Throttle***
	- GKTech eccentric throttle wheel (awesome)

## Maps
I'll be posting my maps here, retaining old versions:

- [Current Map]()
- [Map that uses the CPS, right before I converted to crank sensor](https://drive.google.com/file/d/1FK16yyCmr4FRjlpco8270ERvDUU3UBYU/view?usp=sharing) 

