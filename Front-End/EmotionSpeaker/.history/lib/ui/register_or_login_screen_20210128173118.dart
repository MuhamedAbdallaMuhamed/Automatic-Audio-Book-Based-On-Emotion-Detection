import 'package:EmotionSpeaker/constants/custom_colors.dart';
import 'package:flutter/material.dart';
import 'package:EmotionSpeaker/utils/sizing_extension.dart';

class RegisterOrLoginScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: CustomColors.backgroundColor,
      body: Hero(
        tag: '1',
        child: Center(
          child: Image.asset(
            'assets/audiobook.png',
            height: 50.widthPercentage(context),
            width: 50.widthPercentage(context),
          ),
        ),
      ),
    );
  }
}
