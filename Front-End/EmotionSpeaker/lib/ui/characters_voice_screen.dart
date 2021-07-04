import 'package:EmotionSpeaker/common_widgets/text_input.dart';
import 'package:EmotionSpeaker/models/audio_order.dart';
import 'package:flutter/material.dart';
import 'package:EmotionSpeaker/constants/custom_colors.dart';
import 'package:EmotionSpeaker/utils/sizing_extension.dart';
import 'package:EmotionSpeaker/utils/picker.dart';
import 'package:EmotionSpeaker/common_widgets/rounded_button.dart';
import 'package:EmotionSpeaker/controller/audio_order_controller.dart';
import 'package:EmotionSpeaker/controller/user_controller.dart';
import 'package:get/get.dart';
import 'package:modal_progress_hud/modal_progress_hud.dart';
import 'package:EmotionSpeaker/models/result.dart';

class CharactersVoiceScreen extends StatefulWidget {
  final AudioOrder audioOrder;

  const CharactersVoiceScreen({Key key, this.audioOrder}) : super(key: key);
  @override
  _CharactersVoiceScreenState createState() => _CharactersVoiceScreenState();
}

class _CharactersVoiceScreenState extends State<CharactersVoiceScreen> {
  bool loading = false;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: CustomColors.backgroundColor,
      appBar: AppBar(
        centerTitle: true,
        backgroundColor: CustomColors.color1,
        title: Text(
          "Select Voices",
        ),
      ),
      body: ModalProgressHUD(
        inAsyncCall: loading,
        child: Padding(
          padding: EdgeInsets.all(8.0),
          child: ListView.builder(
            itemCount: widget.audioOrder.charactersNames.length,
            itemBuilder: (context, i) {
              return CharacterRow(
                nameController: TextEditingController(
                    text: widget.audioOrder.charactersNames[i]),
                onTap: (path) {
                  widget.audioOrder.charactersVoices[
                      widget.audioOrder.charactersNames[i]] = path;
                },
                filePath: TextEditingController(),
              );
            },
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
            setState(() {
              loading = true;
            });
            final audioOrderController = Get.find<AudioOrderController>();
            final userController = Get.find<UserController>();
            Result result = await audioOrderController.sendCharacterVoices(
                audioOrder: widget.audioOrder,
                accessToken: userController.mainUser.access_token);
            if (result is SuccessResult) {
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
          },
          textcolor: Colors.white,
        ),
      ),
    );
  }
}

class CharacterRow extends StatefulWidget {
  const CharacterRow({
    Key key,
    this.nameController,
    this.filePath,
    this.onTap,
  }) : super(key: key);
  final TextEditingController nameController;
  final TextEditingController filePath;
  final Function(String path) onTap;

  @override
  _CharacterRowState createState() => _CharacterRowState();
}

class _CharacterRowState extends State<CharacterRow> {
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(4.0),
      child: Container(
        height: 50.hp(context),
        child: Row(
          children: [
            Expanded(
              flex: 1,
              child: TextInput(
                controller: widget.nameController,
                enabled: false,
                textAlign: TextAlign.center,
              ),
            ),
            SizedBox(
              width: 5,
            ),
            Expanded(
              flex: 2,
              child: GestureDetector(
                onTap: () async {
                  String path = await Picker.pickVoice();
                  print(path);
                  widget.filePath.text = path;
                  widget.onTap(path);
                  setState(() {});
                },
                child: TextInput(
                  controller: widget.filePath,
                  enabled: false,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
