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
import 'package:EmotionSpeaker/common_widgets/gender_input.dart';

class RegisterScreen extends StatelessWidget {
  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();
  final TextEditingController firstName = TextEditingController();
  final TextEditingController lastName = TextEditingController();
  final TextEditingController email = TextEditingController();
  final TextEditingController password = TextEditingController();
  final TextEditingController confirmPassword = TextEditingController();
  final TextEditingController phone = TextEditingController();
  final TextEditingController birthDate = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: CustomColors.backgroundColor,
      appBar: AppBar(
        backgroundColor: CustomColors.color1,
        centerTitle: true,
        title: Text(
          'Register',
          style: TextStyle(
            fontFamily: Keys.Araboto,
          ),
        ),
      ),
      body: SafeArea(
        child: SingleChildScrollView(
          child: Form(
            key: _formKey,
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
                  TextInput(
                    validate: TextInput.validateText,
                    controller: firstName,
                  ),
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
                  TextInput(
                    validate: TextInput.validateText,
                    controller: lastName,
                  ),
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
                  PhoneNumberInput(
                    phonecontroller: phone,
                  ),
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
                  TextInput(
                    validate: TextInput.validateText,
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
                    validate: (value) {
                      if (value.isEmpty)
                        return 'Please enter the required information'.tr;
                    },
                    controller: password,
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
                    validate: TextInput.validateText,
                    controller: confirmPassword,
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
                  Stack(
                    children: [
                      TextInput(
                        validate: TextInput.validateText,
                        controller: birthDate,
                      ),
                      ShowCustomDatePicker(
                        controller: birthDate,
                        onChanged: (value) {},
                        startTime: DateTime.now()
                            .subtract(
                              Duration(days: 10000),
                            )
                            .toIso8601String(),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: 1.heightPercentage(context),
                  ),
                  Text(
                    'Gender',
                    style: TextStyle(
                      fontSize: 18.sp(context),
                      fontFamily: Keys.Araboto,
                    ),
                  ),
                  GenderInput(
                    genderStr: (str) {},
                  ),
                  SizedBox(
                    height: 3.heightPercentage(context),
                  ),
                ],
              ),
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
          onPreesed: () {
            if (!_formKey.currentState.validate()) return;
          },
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
