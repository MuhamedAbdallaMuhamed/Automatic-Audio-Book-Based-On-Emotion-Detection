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
  double value = 5.5;
  Duration curDuration;
  RangeValues values = RangeValues(1, 50);
  AudioPlayer audioPlayer = AudioPlayer();

  @override
  void initState() {
    super.initState();
    audioPlayer.play(widget.audioOrder.audioLink);
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
            height: 50.hp(context),
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
                      curDuration = audioPlayer.duration;
                      audioPlayer.pause();
                    } else {
                      audioPlayer.play(widget.audioOrder.audioLink);
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
          SizedBox(
            height: 10.hp(context),
          ),
          /*Slider(
            min: 1,
            max: values.end,
            value: value,
            onChanged: (newvalue) {
              setState(() {
                value = newvalue;
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
                  (value / 4.53).toStringAsFixed(2),
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 20.sp(context),
                  ),
                ),
                Text(
                  "4:53",
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 20.sp(context),
                  ),
                ),
              ],
            ),
          ),*/
        ],
      ),
    );
  }
}
