import 'package:EmotionSpeaker/constants/custom_colors.dart';
import 'package:flutter/material.dart';

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: CustomColors.backgroundColor,
      appBar: AppBar(
        backgroundColor: CustomColors.color1,
        title: Text('Emotion Speaker'),
      ),
    );
  }
}
