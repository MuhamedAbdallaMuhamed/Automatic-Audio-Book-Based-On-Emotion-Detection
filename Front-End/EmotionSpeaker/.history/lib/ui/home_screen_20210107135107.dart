import 'package:EmotionSpeaker/constants/custom_colors.dart';
import 'package:flutter/material.dart';
import 'package:EmotionSpeaker/constants/Keys.dart';

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: CustomColors.backgroundColor,
      appBar: AppBar(
        backgroundColor: CustomColors.color1,
        centerTitle: true,
        title: Text(
          'Emotion Speaker',
          style: TextStyle(
            fontFamily: Keys.Araboto,
          ),
        ),
      ),
    );
  }
}
