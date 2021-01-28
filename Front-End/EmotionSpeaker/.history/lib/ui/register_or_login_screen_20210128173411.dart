import 'package:EmotionSpeaker/common_widgets/rounded_button.dart';
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
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Center(
              child: Image.asset(
                'assets/audiobook.png',
                height: 40.widthPercentage(context),
                width: 40.widthPercentage(context),
              ),
            ),
            RoundedButton(
              title: 'Register',
              buttoncolor: CustomColors.color1,
              onPreesed: () {},
              textcolor: Colors.white,
            ),
          ],
        ),
      ),
    );
  }
}
