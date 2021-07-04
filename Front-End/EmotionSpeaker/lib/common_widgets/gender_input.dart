import 'package:EmotionSpeaker/constants/keys.dart';
import 'package:flutter/material.dart';
import 'package:EmotionSpeaker/utils/sizing_extension.dart';
import 'package:EmotionSpeaker/constants/custom_colors.dart';

enum Gender { male, female }

Gender genderVal = Gender.male;

class GenderInput extends StatefulWidget {
  GenderInput({
    this.gender,
    this.genderStr,
  }) {
    if (gender == 'Male')
      genderVal = Gender.male;
    else
      genderVal = Gender.female;
  }
  final Function(String value) genderStr;
  final String gender;
  @override
  _GenderInputState createState() => _GenderInputState();
}

class _GenderInputState extends State<GenderInput> {
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Row(
          children: [
            SizedBox(
              width: 4.widthPercentage(context),
            ),
            GestureDetector(
              onTap: () {
                setState(() {
                  genderVal = Gender.male;
                  widget.genderStr('Male');
                });
              },
              child: Row(
                children: [
                  Radio(
                    groupValue: genderVal,
                    value: Gender.male,
                    onChanged: (value) {
                      setState(() {
                        genderVal = Gender.male;
                        widget.genderStr('Male');
                      });
                    },
                    activeColor: CustomColors.color1,
                  ),
                  Text(
                    'Male',
                    style: TextStyle(
                      fontFamily: Keys.Araboto,
                      fontSize: 18.sp(context),
                      fontWeight: FontWeight.w100,
                      color: Color(0xff404040),
                    ),
                  ),
                ],
              ),
            ),
            SizedBox(
              width: 10.widthPercentage(context),
            ),
            GestureDetector(
              onTap: () {
                setState(() {
                  genderVal = Gender.female;
                  widget.genderStr('Female');
                });
              },
              child: Row(
                children: [
                  Radio(
                    groupValue: genderVal,
                    value: Gender.female,
                    onChanged: (value) {
                      setState(() {
                        genderVal = value;
                        widget.genderStr('Female');
                      });
                    },
                    activeColor: CustomColors.color1,
                  ),
                  Text(
                    'Female',
                    style: TextStyle(
                      fontFamily: Keys.Araboto,
                      fontSize: 18.sp(context),
                      fontWeight: FontWeight.w100,
                      color: Color(0xff404040),
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ],
    );
  }
}
