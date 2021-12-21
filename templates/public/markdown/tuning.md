The following is for my 7M-GTE running the ECUMasters EMU Black ECU.

## Docs
- [EMU Black Training Manual](https://drive.google.com/file/d/1-_NAlyTh8-dYGTJImPhoPie9wzJ2CXCW/view)
- [EMU Black Reference Manual](https://drive.google.com/file/d/1EdAFo1TTJCEsH4Wx4Oo1ipDlBnCn-KV1/view?usp=sharing)
- Firmware version I am using: [2.126 (test version)](https://www.ecumaster.com/files/EMU_BLACK/EMUBlackSetup_2_136.exe)

## Specs
*If something is not mentioned here, assume it is stock*
### Engine, Electrical
#### ***Sensors*** 
- ***Oxygen***
	- Bosch LSU 4.9 for ECU input
	- Bosch LSU 4.2 for AEM A/F gauge
- ***Trigger***
- ***Pressure***
- ***Temperature***
#### ***Ignition***
- IS300 2JZ-GE waste spark coils using EMU Black internal igniter. ~3ms dwell
#### ***Fuel***
- Bosch 550cc low-Z injectors from Driftmotion
- Using 91-95 Acura Legend 6-channel fuel injector resistor to support sequential injection with low-Z injectors. I should upgrade to larger high-Z injectors eventually so I don't need this resistor.
- Walbro 255, 12V mod. -6AN feed and return
#### ***Boost***
- AUX 4: MAC-type solenoid, AEM 30-2400
#### ***Idle***
- Bosch 2-wire PWM valve 0280140551, plumbed between charge pipe and intake manifold
#### ***Fan***
- 2004 Dodge Stratus fans, made by Bosch
- Ford RR28 PWM fan controllers, one per fan

### Engine, Mechanical
- ***Cylinder Head***
	- **Springs**: Comp Cams 975
- ***Cylinder Block***
- ***Rotating Assembly***
	- **Pistons**: Wiseco 84.5mm
	- **Rods**: Eagle
	- **Bearings**: Taiho, standard size
	- **Harmonic Dampener**: ATI
	- **Clutch**: ACT 3000608 Street Sprung Full-face disc
	- **Driveshaft**: Shaftmasters, aluminum
- ***Turbocharger***
	- Albert Meade 57-trim CT26 (more specs to come)
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

## Maps
I'll be posting my maps here, retaining old versions:

- [Current Map]()
- [Map that uses the CPS, right before I converted to crank sensor](https://drive.google.com/file/d/1FK16yyCmr4FRjlpco8270ERvDUU3UBYU/view?usp=sharing) 

