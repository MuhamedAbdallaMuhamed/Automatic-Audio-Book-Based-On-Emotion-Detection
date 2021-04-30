import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import 'package:EmotionSpeaker/common_widgets/rounded_button.dart';
import 'package:EmotionSpeaker/common_widgets/text_input.dart';
import 'package:EmotionSpeaker/constants/custom_colors.dart';
import 'package:EmotionSpeaker/constants/keys.dart';
import 'package:EmotionSpeaker/utils/sizing_extension.dart';

enum SoundType { defultSound, specialSound }

class NewRequestScreen extends StatefulWidget {
  final String filePath;
  final int pagesNumber;
  final String bookName;
  const NewRequestScreen({
    @required this.filePath,
    @required this.pagesNumber,
    @required this.bookName,
  });
  @override
  _NewRequestScreenState createState() => _NewRequestScreenState();
}

class _NewRequestScreenState extends State<NewRequestScreen> {
  SoundType _soundType = SoundType.defultSound;
  String s = '';

  RangeValues values;
  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();
  final TextEditingController nameTextEditingController =
      TextEditingController();
  @override
  void initState() {
    super.initState();
    values = RangeValues(1, widget.pagesNumber.toDouble());
    nameTextEditingController.text = widget.bookName;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: CustomColors.backgroundColor,
      appBar: AppBar(
        centerTitle: true,
        backgroundColor: CustomColors.color1,
        title: Text(
          "Add Request",
        ),
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: EdgeInsets.symmetric(
            horizontal: 5.widthPercentage(context),
            vertical: 4.heightPercentage(context),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              Text(
                'Book Title',
                style: TextStyle(
                  fontSize: 18.sp(context),
                  fontFamily: Keys.Araboto,
                ),
              ),
              TextInput(
                validate: TextInput.validateText,
                controller: nameTextEditingController,
              ),
              SizedBox(
                height: 15,
              ),
              SizedBox(
                height: 15,
              ),
              Text(
                'Pages Range',
                style: TextStyle(
                  fontSize: 18.sp(context),
                  fontFamily: Keys.Araboto,
                ),
              ),
              Row(
                children: [
                  Text(
                    values.start.toInt().toString(),
                    style: TextStyle(
                      fontSize: 15.sp(context),
                      fontFamily: Keys.Araboto,
                    ),
                  ),
                  SizedBox(
                    width: 2,
                  ),
                  Expanded(
                    child: RangeSlider(
                      onChanged: (value) {
                        setState(() {
                          values = value;
                        });
                      },
                      values: values,
                      min: 1,
                      max: widget.pagesNumber.toDouble(),
                      labels: RangeLabels(
                          values.start.toString(), values.end.toString()),
                      activeColor: CustomColors.color1,
                      inactiveColor: Colors.grey.shade300,
                    ),
                  ),
                  SizedBox(
                    width: 2,
                  ),
                  Text(
                    values.end.toInt().toString(),
                    style: TextStyle(
                      fontSize: 15.sp(context),
                      fontFamily: Keys.Araboto,
                    ),
                  ),
                ],
              ),
              Text(
                'Sound Type:',
                style: TextStyle(
                  fontSize: 18.sp(context),
                  fontFamily: Keys.Araboto,
                ),
              ),
              soundTypeRadio(
                context: context,
                onChanged: (value) {
                  setState(() {
                    _soundType = value;
                  });
                },
                text: 'Defult Sound',
                soundType: SoundType.defultSound,
              ),
              soundTypeRadio(
                context: context,
                onChanged: (value) {
                  setState(() {
                    _soundType = value;
                  });
                },
                text: 'Special Sound',
                soundType: SoundType.specialSound,
              ),
              SizedBox(
                height: 10,
              ),
            ],
          ),
        ),
      ),
      bottomNavigationBar: Padding(
        padding: EdgeInsets.only(
          bottom: 3.heightPercentage(context),
          left: 4.widthPercentage(context),
          right: 4.widthPercentage(context),
        ),
        child: RoundedButton(
          title: 'Submit',
          buttoncolor: CustomColors.color1,
          onPreesed: () async {
            if (!_formKey.currentState.validate()) return;
          },
          textcolor: Colors.white,
        ),
      ),
    );
  }

  Widget soundTypeRadio(
      {BuildContext context,
      String text,
      Function onChanged,
      SoundType soundType}) {
    return GestureDetector(
      onTap: () => onChanged(soundType),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          SizedBox(
            height: 30.0.hp(context),
            width: 20.0.wp(context),
            child: Radio(
              activeColor: CustomColors.color1,
              onChanged: onChanged,
              groupValue: _soundType,
              value: soundType,
            ),
          ),
          SizedBox(
            width: 15.0.wp(context),
          ),
          Text(
            text,
            style: TextStyle(
              fontSize: 18.sp(context),
              fontFamily: Keys.Araboto,
            ),
          ),
        ],
      ),
    );
  }
}
