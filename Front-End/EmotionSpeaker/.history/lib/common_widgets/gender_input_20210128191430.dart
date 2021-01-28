import 'package:EmotionSpeaker/constants/keys.dart';
import 'package:flutter/material.dart';
import 'package:EmotionSpeaker/utils/sizing_extension.dart';
import 'package:EmotionSpeaker/constants/custom_colors.dart';

enum Gender { male, female }

class GenderInput extends StatefulWidget {
  const GenderInput({
    this.genderStr,
  });
  final Function(String value) genderStr;
  @override
  _GenderInputState createState() => _GenderInputState();
}

class _GenderInputState extends State<GenderInput> {
  Gender genderVal;
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
                  widget.genderStr('male');
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
                        widget.genderStr('male');
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
                        widget.genderStr('female');
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
