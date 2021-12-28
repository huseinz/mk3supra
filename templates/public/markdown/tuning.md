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
|  4    |AI &nbsp;#2  |        | 17    |AI &nbsp;#3  |        | 30    |AI &nbsp;#4  |✅A/C SW|
|  5    |CLT          |✅      | 18    |TPS          |✅      | 31    |AI &nbsp;#1  |✅Fuel P|
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
|  4    |AUX #6       |✅CEL   | 12    |AUX #5     |✅PWM Idle| 20    |AUX #4       |✅Tach  |
|  5    |AUX #3    |✅PWM Boost| 13    |AUX #2      |✅PWM Fan| 21    |AUX #1       |✅FP Relay|
|  6    |INJ #4       |✅      | 14    |INJ #5       |✅      | 22    |INJ #6       |✅      |
|  7    |INJ #1       |✅      | 15    |INJ #2       |✅      | 23    |INJ #3       |✅      |
|  8    |IC &nbsp;#1  |✅      | 16    |IC &nbsp;#2  |✅      | 24    |P &nbsp; GND |✅      |

## Specs
*If something is not mentioned here, assume it is stock*
### Engine, Electrical
- ***Sensors*** 
	- ***Trigger***
		Using the Fornari CPS delete kit:
		- **B8**, Primary Trigger (Crank): ZF / Cherry GS100502, 1K pullup
		- **B21**, Camsync In #1: ZF / Cherry GS100701, 1K pullup
	- **Knock**
		- **B3**, **B16**: Bosch donut (EV1 connector)
	- ***Oxygen***
		- Bosch LSU 4.2 for AEM 30-4100 A/F gauge
		- Bosch LSU 4.9 for ECU input
	- ***Pressure***
		- **B31** Fuel: LDM 0-100psi, mounted in AFPR gauge port
		- **B35**: Oil: LDM 0-100psi, mounted at the '7M' inscription port
		- Factory sender and factory gauge
	- ***Temperature***
		- **B5** CLT: 89+ Toyota sensor, stock sensor port
		- **B32** IAT: Bosch 0280130085, mounted in 3000 pipe
		- **B37** Oil: AEM 30-2012, placed pre-filter at oil pump outlet
- ***Ignition***
	- **Coils**: IS300 2JZ-GE waste-spark coils using EMU Black internal igniter. ~3ms dwell
- ***Fuel***
	- **G21**, **Pump**: Walbro 255, 12V relay mod, -6AN feed and return
	- **AFPR**: DeatschWerks DWR1000i 50psi @ atmospheric
	- **Injectors**: Bosch 550cc low-Z injectors from Driftmotion. 91-95 Acura Legend 6-channel fuel injector resistor to support sequential injection with low-Z injectors
- ***Boost Control***
	- **G5**: AEM 30-2400 (MAC VSV)
- ***Idle Control***
	- **G12**: Bosch 0280140551, 2-wire PWM valve, plumbed between charge pipe and intake manifold
- ***Cooling***
	- **G13**: Ford Motorcraft RR28 PWM fan controllers, one per fan
- ***Gauges***
	- **Boost/Vacuum**: AEM 30-4350 Tru-Boost
	- **A/F Ratio**: AEM 30-4100 Wideband UEGO
	- **Others**: Head unit display via CAN

### Engine, Mechanical
- ***Cylinder Head***
	- **Springs**: BC
	- **Head Gasket**: Cometic
	- **Head Studs**: ARP
- ***Cylinder Block***
	- **Main Studs**: ARP
	- **Main Bearings**: Taiho, standard
- ***Rotating Assembly***
	- **Pistons**: Wiseco 84.5mm
	- **Rods**: Eagle
	- **Bearings**: Taiho, standard
	- **Harmonic Dampener**: ATI Super Damper 918525
	- **Trigger Wheel**: Fornari 36-1
	- **Clutch**: ACT 3000608 Street sprung full-face disc
	- **Pressure Plate**: it's an OEM housing painted red, so I assume it's been 'upgraded' but not sure by whomst
	- **Driveshaft**: Shaftmasters, aluminum
- ***Turbocharger***
	- Albert Meade 57-trim CT26 (more specs to come)
- ***Intake***
	- **Piping**: 2.5" universal aluminum piping and couplers
	- **BOV**: HKS SSQV clone
	- **Intercooler**: Spearco clone
- ***Exhaust***
	- **Downpipe**: Driftmotion CT-26 bellmouth downpipe
	- **Piping**: RS-R Japan 3"
	- **Resonator**: Vibrant 1142 Ultra-Quiet
- ***Lubrication***
	- **Filter Housing**: Driftmotion billet remote-oil filter kit with -10AN lines
	- **Oil Cooler**: Setrab thermostatic sandwich plate
- ***Cooling***
	- **Fan**: 2004 Dodge Stratus fans, made by Bosch
	- **Radiator**: GPI Racing 3-row aluminum
	- **Cap**: HKS 15009-AK004 1.1bar
- ***Throttle***
	- GKTech S13/S14 eccentric throttle cable wheel (awesome)

## Maps
I'll be posting my maps here, retaining old versions:

- [Current Map]()
- [Map that uses the CPS, right before I converted to crank sensor](https://drive.google.com/file/d/1FK16yyCmr4FRjlpco8270ERvDUU3UBYU/view?usp=sharing) 

