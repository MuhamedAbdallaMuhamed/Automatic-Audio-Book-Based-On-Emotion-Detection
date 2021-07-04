import 'package:EmotionSpeaker/models/audio_order.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:EmotionSpeaker/models/result.dart';
import 'package:EmotionSpeaker/common_widgets/rounded_button.dart';
import 'package:EmotionSpeaker/common_widgets/text_input.dart';
import 'package:EmotionSpeaker/constants/custom_colors.dart';
import 'package:EmotionSpeaker/constants/keys.dart';
import 'package:EmotionSpeaker/utils/sizing_extension.dart';
import 'package:pdf_text/pdf_text.dart';
import 'package:EmotionSpeaker/controller/audio_order_controller.dart';
import 'package:EmotionSpeaker/controller/user_controller.dart';
import 'package:get/get.dart';
import 'package:modal_progress_hud/modal_progress_hud.dart';

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
  final TextEditingController titleTextEditingController =
      TextEditingController();
  bool loading = false;
  @override
  void initState() {
    super.initState();
    values = RangeValues(1, widget.pagesNumber.toDouble());
    titleTextEditingController.text = widget.bookName;
  }

  @override
  Widget build(BuildContext context) {
    return Form(
      key: _formKey,
      child: Scaffold(
        backgroundColor: CustomColors.backgroundColor,
        appBar: AppBar(
          centerTitle: true,
          backgroundColor: CustomColors.color1,
          title: Text(
            "Add Request",
          ),
        ),
        body: ModalProgressHUD(
          inAsyncCall: loading,
          child: SingleChildScrollView(
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
                    controller: titleTextEditingController,
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
                    text: 'Default Sound',
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
            onPreesed: onSubmit,
            textcolor: Colors.white,
          ),
        ),
      ),
    );
  }

  onSubmit() async {
    if (!_formKey.currentState.validate()) return;
    setState(() {
      loading = true;
    });
    AudioOrder audioOrder = AudioOrder();
    audioOrder.title = titleTextEditingController.text;
    audioOrder.cloned = _soundType == SoundType.defultSound ? 0 : 1;
    audioOrder.startPage = values.start.toInt();
    audioOrder.endPage = values.end.toInt();
    audioOrder.text = [];
    print(values.start);
    print(values.end);
    PDFDoc doc = await PDFDoc.fromPath(widget.filePath);

    for (int i = (values.start).toInt(); i <= (values.end).toInt(); i++) {
      PDFPage page = doc.pageAt(i);
      String text = await page.text;
      audioOrder.text.add(text);
    }
    print(audioOrder.toJson());
    final userController = Get.find<UserController>();
    final audioOrderController = Get.find<AudioOrderController>();
    Result result = await audioOrderController.addAudioOrder(
        audioOrder: audioOrder,
        accessToken: userController.mainUser.access_token);
    if (result is SuccessResult) {
      Get.back();
      Get.back();
    } else {
      await Get.defaultDialog(
        title: 'Error',
        middleText: result.getErrorMessage(),
      );
    }
    setState(() {
      loading = false;
    });
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
