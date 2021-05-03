import os
from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from gateway import gateway
from pydub import AudioSegment

app = Flask(__name__)
app.config["FILE_UPLOADS"] = os.path.dirname(os.path.realpath(__file__))
app.config["ALLOWED_FILE_EXTENSIONS"] = ["WAV", "OGG"]
app.config["SENTENCE"] = "text"
app.config["FILE"] = "file"
app.config["FILE_SIZE"] = "file_size"
app.config["MAX_FILE_SIZE"] = 1024 * 1024
app.config["FILE_PATH"] = os.path.dirname(os.path.realpath(__file__))
output_file = list()


def allowed_file(filename):
    if not ("." in filename) or filename == "":
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_FILE_EXTENSIONS"]:
        return True
    else:
        return False


def allowed_file_size(file_size):
    if int(file_size) <= app.config["MAX_FILE_SIZE"]:
        return True
    else:
        return False


def mem_clean_up():
    for i in output_file:
        os.unlink(os.path.join(app.config["FILE_PATH"], i))
    output_file.clear()


def slow_down(sound, speed=1.0):
    return sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})


@app.route("/TTS", methods=['GET'])
def TTS():
    sentences = str(request.form[app.config["SENTENCE"]])
    file_size = int(request.form[app.config["FILE_SIZE"]])
    file = request.files[app.config["FILE"]]
    mem_clean_up()
    try:
        if allowed_file_size(file_size) and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["FILE_UPLOADS"], filename))
            file_path = gateway(os.path.join(app.config["FILE_UPLOADS"], filename), sentences)
            if file_path != "":
                sound = AudioSegment.from_file(os.path.join(app.config["FILE_PATH"], file_path))
                slower_sound = slow_down(sound)
                slower_file_path = os.path.join(app.config["FILE_PATH"], file_path + 'slower.wav')
                slower_file_name = file_path + 'slower.wav'
                slower_sound.export(slower_file_path, format="wav")
                output_file.append(slower_file_name)
                os.unlink(file_path)
                return send_from_directory(app.config["FILE_PATH"], filename=slower_file_name, as_attachment=True)
    except Exception as error:
        print(error)
    return jsonify({"response": "error"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)
