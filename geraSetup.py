import cx_Freeze
executables = [
    cx_Freeze.Executable(script="main.py", icon="flappybird.ico")
]
cx_Freeze.setup(
    name = "FlappyBird",
    options = {
        "build_exe":{
            "packages": ["pygame"],
            "include_files": [
                "fundo.jpg",
                "flappybird.png"
            ]
        }
    } , executables = executables
)
# python geraSetup.py build
# python geraSetup.py bdist_msi