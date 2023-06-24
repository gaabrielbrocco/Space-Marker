import cx_Freeze
executables = [
    cx_Freeze.Executable(script="main.py", icon="rocket.png")
]
cx_Freeze.setup(
    name = "Space Marker",
    options = {
        "build_exe":{
            "packages": ["pygame"],
            "include_files": [
                "background.jpg",
                "rocket.png",
                "estrelas_salvas.txt",
                "eletroMusic.mp3",
                "main.py"

                
            ]
        }
    } , executables = executables
)
# python geraSetup.py build
# python geraSetup.py bdist_msi