# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Version 2024.1.0
# 19:08:54  Jul 15, 2026
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("EMI_SNP")
oDesign = oProject.SetActiveDesign("0_EMI_SINGLE")
oModule = oDesign.GetModule("ReportSetup")
oModule.AddCartesianXMarker("GOLDRIVER", "MX1", 0)
oModule.DeleteDrawing([])
oDesign = oProject.SetActiveDesign("0_EMI_SINGLE_BROADBAND")
oModule = oDesign.GetModule("ReportSetup")
oModule.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Scaling",
			[
				"NAME:PropServers", 
				"GoldRiver_20260715:AxisY1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Units",
					"Value:="		, "ohm"
				]
			]
		]
	])
oModule.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Scaling",
			[
				"NAME:PropServers", 
				"GoldRiver_20260715:AxisY1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Auto Units",
					"Value:="		, False
				],
				[
					"NAME:Units",
					"Value:="		, "ohm"
				]
			]
		]
	])
oDesign = oProject.SetActiveDesign("0_EMI_SINGLE")
oModule = oDesign.GetModule("ReportSetup")
oModule.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Scaling",
			[
				"NAME:PropServers", 
				"GOLDRIVER:AxisY1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Auto Units",
					"Value:="		, False
				],
				[
					"NAME:Units",
					"Value:="		, "ohm"
				]
			]
		]
	])
