PULSONIX_LIBRARY_ASCII "SamacSys ECAD Model"
//474910/1062820/2.50/6/2/Connector

(asciiHeader
	(fileUnits MM)
)
(library Library_1
	(padStyleDef "c165_h110"
		(holeDiam 1.1)
		(padShape (layerNumRef 1) (padShapeType Ellipse)  (shapeWidth 1.65) (shapeHeight 1.65))
		(padShape (layerNumRef 16) (padShapeType Ellipse)  (shapeWidth 1.65) (shapeHeight 1.65))
	)
	(padStyleDef "s165_h110"
		(holeDiam 1.1)
		(padShape (layerNumRef 1) (padShapeType Rect)  (shapeWidth 1.65) (shapeHeight 1.65))
		(padShape (layerNumRef 16) (padShapeType Rect)  (shapeWidth 1.65) (shapeHeight 1.65))
	)
	(textStyleDef "Normal"
		(font
			(fontType Stroke)
			(fontFace "Helvetica")
			(fontHeight 1.27)
			(strokeWidth 0.127)
		)
	)
	(patternDef "RHDRRA6W64P254_1X6_1575X851X24" (originalName "RHDRRA6W64P254_1X6_1575X851X24")
		(multiLayer
			(pad (padNum 1) (padStyleRef s165_h110) (pt 0, 0) (rotation 90))
			(pad (padNum 2) (padStyleRef c165_h110) (pt -2.54, 0) (rotation 90))
			(pad (padNum 3) (padStyleRef c165_h110) (pt -5.08, 0) (rotation 90))
			(pad (padNum 4) (padStyleRef c165_h110) (pt -7.62, 0) (rotation 90))
			(pad (padNum 5) (padStyleRef c165_h110) (pt -10.16, 0) (rotation 90))
			(pad (padNum 6) (padStyleRef c165_h110) (pt -12.7, 0) (rotation 90))
		)
		(layerContents (layerNumRef 18)
			(attr "RefDes" "RefDes" (pt 0, 0) (textStyleRef "Normal") (isVisible True))
		)
		(layerContents (layerNumRef Courtyard_Top)
			(line (pt 1.775 -1.325) (pt -14.475 -1.325) (width 0.05))
		)
		(layerContents (layerNumRef Courtyard_Top)
			(line (pt -14.475 -1.325) (pt -14.475 10.28) (width 0.05))
		)
		(layerContents (layerNumRef Courtyard_Top)
			(line (pt -14.475 10.28) (pt 1.775 10.28) (width 0.05))
		)
		(layerContents (layerNumRef Courtyard_Top)
			(line (pt 1.775 10.28) (pt 1.775 -1.325) (width 0.05))
		)
		(layerContents (layerNumRef 28)
			(line (pt 1.525 1.52) (pt -14.225 1.52) (width 0.025))
		)
		(layerContents (layerNumRef 28)
			(line (pt -14.225 1.52) (pt -14.225 10.03) (width 0.025))
		)
		(layerContents (layerNumRef 28)
			(line (pt -14.225 10.03) (pt 1.525 10.03) (width 0.025))
		)
		(layerContents (layerNumRef 28)
			(line (pt 1.525 10.03) (pt 1.525 1.52) (width 0.025))
		)
		(layerContents (layerNumRef 18)
			(line (pt 1.525 0) (pt 1.525 10.03) (width 0.2))
		)
		(layerContents (layerNumRef 18)
			(line (pt 1.525 10.03) (pt -14.225 10.03) (width 0.2))
		)
		(layerContents (layerNumRef 18)
			(line (pt -14.225 10.03) (pt -14.225 1.52) (width 0.2))
		)
	)
	(symbolDef "SSQ-106-02-G-S-RA" (originalName "SSQ-106-02-G-S-RA")

		(pin (pinNum 1) (pt 0 mils 0 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -25 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 2) (pt 0 mils -100 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -125 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 3) (pt 0 mils -200 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -225 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 4) (pt 0 mils -300 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -325 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 5) (pt 0 mils -400 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -425 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 6) (pt 0 mils -500 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -525 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(line (pt 200 mils 100 mils) (pt 600 mils 100 mils) (width 6 mils))
		(line (pt 600 mils 100 mils) (pt 600 mils -600 mils) (width 6 mils))
		(line (pt 600 mils -600 mils) (pt 200 mils -600 mils) (width 6 mils))
		(line (pt 200 mils -600 mils) (pt 200 mils 100 mils) (width 6 mils))
		(attr "RefDes" "RefDes" (pt 650 mils 300 mils) (justify Left) (isVisible True) (textStyleRef "Normal"))
		(attr "Type" "Type" (pt 650 mils 200 mils) (justify Left) (isVisible True) (textStyleRef "Normal"))

	)
	(compDef "SSQ-106-02-G-S-RA" (originalName "SSQ-106-02-G-S-RA") (compHeader (numPins 6) (numParts 1) (refDesPrefix J)
		)
		(compPin "1" (pinName "1") (partNum 1) (symPinNum 1) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "2" (pinName "2") (partNum 1) (symPinNum 2) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "3" (pinName "3") (partNum 1) (symPinNum 3) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "4" (pinName "4") (partNum 1) (symPinNum 4) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "5" (pinName "5") (partNum 1) (symPinNum 5) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "6" (pinName "6") (partNum 1) (symPinNum 6) (gateEq 0) (pinEq 0) (pinType Unknown))
		(attachedSymbol (partNum 1) (altType Normal) (symbolName "SSQ-106-02-G-S-RA"))
		(attachedPattern (patternNum 1) (patternName "RHDRRA6W64P254_1X6_1575X851X24")
			(numPads 6)
			(padPinMap
				(padNum 1) (compPinRef "1")
				(padNum 2) (compPinRef "2")
				(padNum 3) (compPinRef "3")
				(padNum 4) (compPinRef "4")
				(padNum 5) (compPinRef "5")
				(padNum 6) (compPinRef "6")
			)
		)
		(attr "Mouser Part Number" "200-SSQ10602GSRA")
		(attr "Mouser Price/Stock" "https://www.mouser.co.uk/ProductDetail/Samtec/SSQ-106-02-G-S-RA?qs=rU5fayqh%252BE34S8VhbDAmgg%3D%3D")
		(attr "Manufacturer_Name" "SAMTEC")
		(attr "Manufacturer_Part_Number" "SSQ-106-02-G-S-RA")
		(attr "Description" "Samtec SSQ Series 2.54mm 6 Way 1 Row Right Angle PCB Socket Through Hole Board to Board")
		(attr "<Hyperlink>" "http://suddendocs.samtec.com/catalog_english/ssq_th.pdf")
		(attr "<Component Height>" "2.41")
		(attr "<STEP Filename>" "SSQ-106-02-G-S-RA.stp")
		(attr "<STEP Offsets>" "X=0;Y=0;Z=0")
		(attr "<STEP Rotation>" "X=0;Y=0;Z=0")
	)

)