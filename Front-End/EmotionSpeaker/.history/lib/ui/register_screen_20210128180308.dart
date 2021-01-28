import 'package:EmotionSpeaker/common_widgets/text_input.dart';
import 'package:EmotionSpeaker/common_widgets/rounded_button.dart';
import 'package:EmotionSpeaker/constants/custom_colors.dart';
import 'package:EmotionSpeaker/constants/keys.dart';
import 'package:EmotionSpeaker/ui/home_screen.dart';
import 'package:flutter/material.dart';
import 'package:EmotionSpeaker/utils/sizing_extension.dart';
import 'package:get/get.dart';
import 'package:EmotionSpeaker/common_widgets/phone_number_input.dart';

class RegisterScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: CustomColors.backgroundColor,
      body: SafeArea(
        child: SingleChildScrollView(
          child: Padding(
            padding: EdgeInsets.symmetric(
              horizontal: 5.widthPercentage(context),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                SizedBox(
                  height: 2.heightPercentage(context),
                ),
                Center(
                  child: Image.asset(
                    'assets/audiobook.png',
                    height: 30.widthPercentage(context),
                    width: 30.widthPercentage(context),
                  ),
                ),
                Center(
                  child: Text(
                    'Register',
                    style: TextStyle(
                      fontSize: 30.sp(context),
                      fontFamily: Keys.Araboto,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
                SizedBox(
                  height: 2.heightPercentage(context),
                ),
                Text(
                  'First Name',
                  style: TextStyle(
                    fontSize: 18.sp(context),
                    fontFamily: Keys.Araboto,
                  ),
                ),
                TextInput(),
                SizedBox(
                  height: 1.heightPercentage(context),
                ),
                Text(
                  'Last Name',
                  style: TextStyle(
                    fontSize: 18.sp(context),
                    fontFamily: Keys.Araboto,
                  ),
                ),
                TextInput(),
                SizedBox(
                  height: 1.heightPercentage(context),
                ),
                Text(
                  'Email',
                  style: TextStyle(
                    fontSize: 18.sp(context),
                    fontFamily: Keys.Araboto,
                  ),
                ),
                TextInput(),
                SizedBox(
                  height: 1.heightPercentage(context),
                ),
                Text(
                  'Password',
                  style: TextStyle(
                    fontSize: 18.sp(context),
                    fontFamily: Keys.Araboto,
                  ),
                ),
                TextInput(
                  obscure: true,
                ),
                PhoneNumberInput(),
                SizedBox(
                  height: 1.heightPercentage(context),
                ),
                SizedBox(
                  height: 2.heightPercentage(context),
                ),
                RoundedButton(
                  title: 'Sign In',
                  buttoncolor: CustomColors.color1,
                  onPreesed: () {},
                  textcolor: Colors.white,
                ),
                SizedBox(
                  height: 2.heightPercentage(context),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  signinwithGoogle() {
    Get.to(HomeScreen());
  }

  signinwithFacebbok() {
    Get.to(HomeScreen());
  }
}
