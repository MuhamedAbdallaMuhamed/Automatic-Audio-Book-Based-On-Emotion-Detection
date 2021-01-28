import 'package:EmotionSpeaker/common_widgets/text_input.dart';
import 'package:EmotionSpeaker/common_widgets/rounded_button.dart';
import 'package:EmotionSpeaker/constants/custom_colors.dart';
import 'package:EmotionSpeaker/constants/keys.dart';
import 'package:EmotionSpeaker/controller/user_controller.dart';
import 'package:flutter/material.dart';
import 'package:EmotionSpeaker/utils/sizing_extension.dart';
import 'package:get/get.dart';

class SigninScreen extends StatelessWidget {
  final userController = Get.find<UserController>();
  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();
  final TextEditingController email = TextEditingController();
  final TextEditingController password = TextEditingController();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: CustomColors.backgroundColor,
      body: Form(
        key: _formKey,
        child: SingleChildScrollView(
          child: Padding(
            padding: EdgeInsets.symmetric(
              horizontal: 10.widthPercentage(context),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                SizedBox(
                  height: 10.heightPercentage(context),
                ),
                Center(
                  child: Hero(
                    tag: '1',
                    transitionOnUserGestures: true,
                    child: Image.asset(
                      'assets/audiobook.png',
                      height: 30.widthPercentage(context),
                      width: 30.widthPercentage(context),
                    ),
                  ),
                ),
                SizedBox(
                  height: 1.heightPercentage(context),
                ),
                Center(
                  child: Text(
                    'Sign In',
                    style: TextStyle(
                      fontSize: 30.sp(context),
                      fontFamily: Keys.Araboto,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
                SizedBox(
                  height: 5.heightPercentage(context),
                ),
                Text(
                  'Email',
                  style: TextStyle(
                    fontSize: 18.sp(context),
                    fontFamily: Keys.Araboto,
                  ),
                ),
                TextInput(
                  validate: TextInput.validateMail,
                  controller: email,
                ),
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
                  validate: TextInput.validateText,
                  controller: password,
                ),
                SizedBox(
                  height: 2.heightPercentage(context),
                ),
                RoundedButton(
                  title: 'Sign In',
                  buttoncolor: CustomColors.color1,
                  onPreesed: () {
                    if (!_formKey.currentState.validate()) return;
                    String emailStr = email.text;
                    String password = password.text;
                  },
                  textcolor: Colors.white,
                ),
                SizedBox(
                  height: 2.heightPercentage(context),
                ),
                Row(
                  mainAxisAlignment: MainAxisAlignment.end,
                  children: [
                    Expanded(
                      child: Container(
                        height: 2,
                        color: Colors.grey,
                      ),
                    ),
                    Padding(
                      padding: EdgeInsets.symmetric(
                        horizontal: 2.widthPercentage(context),
                      ),
                      child: Text(
                        'OR',
                        style: TextStyle(
                          fontSize: 15.sp(context),
                          fontFamily: Keys.Araboto,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ),
                    Expanded(
                      child: Container(
                        height: 2,
                        color: Colors.grey,
                      ),
                    )
                  ],
                ),
                SizedBox(
                  height: 2.heightPercentage(context),
                ),
                Center(
                  child: Text(
                    'Sign In with',
                    style: TextStyle(
                      fontSize: 15.sp(context),
                      fontFamily: Keys.Araboto,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
                SizedBox(
                  height: 2.heightPercentage(context),
                ),
                RoundedButton(
                  title: 'Facebook',
                  buttoncolor: Color(0xff355ba9),
                  onPreesed: signinwithFacebbok,
                  textcolor: Colors.white,
                ),
                SizedBox(
                  height: 2.heightPercentage(context),
                ),
                RoundedButton(
                  title: 'Google',
                  buttoncolor: Colors.grey.shade300,
                  onPreesed: signinwithGoogle,
                  textcolor: Colors.black,
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  signinwithGoogle() {
    // Get.to(HomeScreen());
  }

  signinwithFacebbok() {
    //  Get.to(HomeScreen());
  }
}
