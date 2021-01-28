import 'package:EmotionSpeaker/common_widgets/date_picker.dart';
import 'package:EmotionSpeaker/common_widgets/profile_picture.dart';
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
      appBar: AppBar(title:  Text(
                    'Register',
                    style: TextStyle(
                      fontSize: 30.sp(context),
                      fontFamily: Keys.Araboto,
                      fontWeight: FontWeight.bold,
                    ),
                  ),,),
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
                SizedBox(
                  height: 1.heightPercentage(context),
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
                ProfilePicture(
                  fileFun: (file) {},
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
                  'Phone',
                  style: TextStyle(
                    fontSize: 18.sp(context),
                    fontFamily: Keys.Araboto,
                  ),
                ),
                PhoneNumberInput(),
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
                SizedBox(
                  height: 1.heightPercentage(context),
                ),
                Text(
                  'Confirm Password',
                  style: TextStyle(
                    fontSize: 18.sp(context),
                    fontFamily: Keys.Araboto,
                  ),
                ),
                TextInput(
                  obscure: true,
                ),
                SizedBox(
                  height: 1.heightPercentage(context),
                ),
                Text(
                  'Birth Date',
                  style: TextStyle(
                    fontSize: 18.sp(context),
                    fontFamily: Keys.Araboto,
                  ),
                ),
                ShowCustomDatePicker(
                  onChanged: (value) {},
                  startTime: DateTime.now()
                      .subtract(
                        Duration(days: 10000),
                      )
                      .toIso8601String(),
                ),
                SizedBox(
                  height: 3.heightPercentage(context),
                ),
              ],
            ),
          ),
        ),
      ),
      bottomNavigationBar: Padding(
        padding: EdgeInsets.only(
            bottom: 2.heightPercentage(context),
            left: 2.widthPercentage(context),
            right: 2.widthPercentage(context)),
        child: RoundedButton(
          title: 'Register',
          buttoncolor: CustomColors.color1,
          onPreesed: () {},
          textcolor: Colors.white,
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
