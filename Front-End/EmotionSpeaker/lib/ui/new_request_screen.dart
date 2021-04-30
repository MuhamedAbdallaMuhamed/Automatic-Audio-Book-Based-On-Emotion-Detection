import 'package:flutter/material.dart';
import 'package:EmotionSpeaker/constants/custom_colors.dart';
import 'package:EmotionSpeaker/constants/keys.dart';
import 'package:EmotionSpeaker/common_widgets/text_input.dart';
import 'package:EmotionSpeaker/utils/sizing_extension.dart';
import 'package:EmotionSpeaker/common_widgets/rounded_button.dart';
import 'package:EmotionSpeaker/utils/picker.dart';
import 'package:pdf_text/pdf_text.dart';

enum SoundType { defultSound, specialSound }

class NewRequestScreen extends StatefulWidget {
  @override
  _NewRequestScreenState createState() => _NewRequestScreenState();
}

class _NewRequestScreenState extends State<NewRequestScreen> {
  SoundType _soundType = SoundType.defultSound;
  String s = '';
  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();

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
              ),
              SizedBox(
                height: 15,
              ),
              Text(
                'Book',
                style: TextStyle(
                  fontSize: 18.sp(context),
                  fontFamily: Keys.Araboto,
                ),
              ),
              RaisedButton(
                onPressed: pickFile,
                child: Icon(
                  Icons.upload_file,
                  size: 25,
                  color: Colors.white,
                ),
                color: CustomColors.color1,
                padding: EdgeInsets.all(10),
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
              Padding(
                padding: EdgeInsets.symmetric(
                  horizontal: 10,
                  vertical: 5,
                ),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceAround,
                  children: [
                    Text(
                      'Start',
                      style: TextStyle(
                        fontSize: 18.sp(context),
                        fontFamily: Keys.Araboto,
                      ),
                    ),
                    Expanded(
                      child: Padding(
                        padding: EdgeInsets.symmetric(horizontal: 5),
                        child: TextInput(
                          validate: TextInput.validateText,
                        ),
                      ),
                    ),
                    SizedBox(
                      width: 10,
                    ),
                    Text(
                      'End',
                      style: TextStyle(
                        fontSize: 18.sp(context),
                        fontFamily: Keys.Araboto,
                      ),
                    ),
                    Expanded(
                      child: Padding(
                        padding: EdgeInsets.symmetric(horizontal: 5),
                        child: TextInput(
                          validate: TextInput.validateText,
                        ),
                      ),
                    ),
                  ],
                ),
              ),
              SizedBox(
                height: 10,
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

  void pickFile() async {
    String filePath = await Picker.pickFile();
    print(filePath);
    PDFDoc doc = await PDFDoc.fromPath(filePath);
    PDFPage page = doc.pageAt(5);
    setState(() async {
      s = await page.text;
    });
    //  print(s);
    print(s.length);

    print('done');
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
