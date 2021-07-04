import 'package:EmotionSpeaker/constants/keys.dart';
import 'package:EmotionSpeaker/models/audio_order.dart';
import 'package:audioplayer/audioplayer.dart';
import 'package:flutter/material.dart';
import 'package:EmotionSpeaker/constants/custom_colors.dart';
import 'package:EmotionSpeaker/utils/sizing_extension.dart';

class AudioPlayerScreen extends StatefulWidget {
  final AudioOrder audioOrder;

  const AudioPlayerScreen({Key key, this.audioOrder}) : super(key: key);
  @override
  _AudioPlayerScreenState createState() => _AudioPlayerScreenState();
}

class _AudioPlayerScreenState extends State<AudioPlayerScreen> {
  bool voiceOn = true;
  double value = 0;
  Duration curDuration = Duration();
  RangeValues values = RangeValues(0, 10000000000000000000000);
  AudioPlayer audioPlayer = AudioPlayer();

  @override
  void initState() {
    super.initState();
    play();
  }

  void play() async {
    await audioPlayer.play(widget.audioOrder.audioLink);

    audioPlayer.onAudioPositionChanged.listen((p) => setState(() {
          values = RangeValues(0, audioPlayer.duration.inSeconds.toDouble());
          value = p.inSeconds.toDouble();
          print(value);
          print(audioPlayer.duration.inSeconds.toDouble());
          print(values);
          if (p.inSeconds >= audioPlayer.duration.inSeconds) voiceOn = false;

          return curDuration = p;
        }));
  }

  @override
  void dispose() {
    super.dispose();
    audioPlayer.stop();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: CustomColors.color2,
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.center,
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Center(
            child: Icon(
              Icons.book,
              color: CustomColors.backgroundColor,
              size: 200.sp(context),
            ),
          ),
          Text(
            widget.audioOrder.title,
            style: TextStyle(
              fontFamily: Keys.Araboto,
              fontSize: 30.sp(context),
              fontWeight: FontWeight.bold,
              color: CustomColors.backgroundColor,
            ),
          ),
          SizedBox(
            height: 10.hp(context),
          ),
          Text(
            "From Page ${widget.audioOrder.startPage} to Page ${widget.audioOrder.endPage}",
            style: TextStyle(
              fontFamily: Keys.Araboto,
              fontSize: 25.sp(context),
              color: CustomColors.backgroundColor,
            ),
          ),
          SizedBox(
            height: 100.hp(context),
          ),
          Slider(
            min: values.start,
            max: values.end,
            value: value,
            onChanged: (newvalue) {
              setState(() async {
                value = newvalue;
                await audioPlayer.seek(value);
                voiceOn = true;
              });
            },
            activeColor: CustomColors.color1,
            inactiveColor: CustomColors.backgroundColor,
          ),
          Padding(
            padding: EdgeInsets.symmetric(
              horizontal: 6.widthPercentage(context),
              vertical: 0,
            ),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text(
                  (curDuration.inMinutes.toString() +
                          ':' +
                          curDuration.inSeconds.toString()) ??
                      "00:00",
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 20.sp(context),
                  ),
                ),
                Text(
                  (audioPlayer.duration.inMinutes.toString() +
                          ':' +
                          audioPlayer.duration.inSeconds.toString()) ??
                      "00:00",
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 20.sp(context),
                  ),
                ),
              ],
            ),
          ),
          SizedBox(
            height: 10.hp(context),
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              IconButton(
                padding: EdgeInsets.all(0),
                color: CustomColors.color3,
                onPressed: () {
                  setState(() {
                    if (voiceOn) {
                      audioPlayer.pause();
                    } else {
                      audioPlayer.play(widget.audioOrder.audioLink);
                      audioPlayer.seek(value % audioPlayer.duration.inSeconds);
                    }
                    voiceOn = !voiceOn;
                  });
                },
                icon: Container(
                  decoration: BoxDecoration(
                    color: CustomColors.backgroundColor,
                    shape: BoxShape.circle,
                  ),
                  child: Padding(
                    padding: EdgeInsets.all(8.0),
                    child: Icon(
                      !voiceOn ? Icons.play_arrow : Icons.pause,
                      color: CustomColors.color2,
                      size: 35.sp(context),
                    ),
                  ),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
