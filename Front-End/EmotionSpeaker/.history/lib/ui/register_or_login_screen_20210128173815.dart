import 'package:EmotionSpeaker/common_widgets/rounded_button.dart';
import 'package:EmotionSpeaker/constants/custom_colors.dart';
import 'package:EmotionSpeaker/ui/signin_screen.dart';
import 'package:flutter/material.dart';
import 'package:EmotionSpeaker/utils/sizing_extension.dart';
import 'package:get/get.dart';

class RegisterOrLoginScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: CustomColors.backgroundColor,
      body: Hero(
        tag: '1',
        child: Padding(
          padding: EdgeInsets.all(10.widthPercentage(context)),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Center(
                child: Image.asset(
                  'assets/audiobook.png',
                  height: 40.widthPercentage(context),
                  width: 40.widthPercentage(context),
                ),
              ),
              SizedBox(
                height: 5.heightPercentage(context),
              ),
              RoundedButton(
                title: 'Register',
                buttoncolor: CustomColors.color1,
                onPreesed: () {},
                textcolor: Colors.white,
              ),
              SizedBox(
                height: 2.heightPercentage(context),
              ),
              RoundedButton(
                title: 'Sign in',
                buttoncolor: CustomColors.color2,
                onPreesed: () {
                  Get.to(SigninScreen());
                },
                textcolor: Colors.white,
              ),
            ],
          ),
        ),
      ),
    );
  }
}
