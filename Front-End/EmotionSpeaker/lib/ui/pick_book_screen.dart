import 'package:EmotionSpeaker/constants/custom_colors.dart';
import 'package:EmotionSpeaker/constants/keys.dart';
import 'package:EmotionSpeaker/ui/new_request_screen.dart';
import 'package:EmotionSpeaker/utils/picker.dart';
import 'package:flutter/material.dart';
import 'package:EmotionSpeaker/utils/sizing_extension.dart';
import 'package:get/get.dart';
import 'package:modal_progress_hud/modal_progress_hud.dart';
import 'package:pdf_text/pdf_text.dart';
import 'package:path/path.dart';

class PickBookScreen extends StatefulWidget {
  @override
  _PickBookScreenState createState() => _PickBookScreenState();
}

class _PickBookScreenState extends State<PickBookScreen> {
  bool loading = false;
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
      body: ModalProgressHUD(
        inAsyncCall: loading,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Center(
              child: Text(
                "Select Book",
                style: TextStyle(
                  fontSize: 25.sp(context),
                  fontFamily: Keys.Araboto,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
            SizedBox(
              height: 5,
            ),
            Center(
              child: RaisedButton(
                onPressed: pickFile,
                padding: EdgeInsets.all(0),
                child: Container(
                  height: 40.widthPercentage(context),
                  width: 40.widthPercentage(context),
                  decoration: BoxDecoration(
                    color: CustomColors.color1,
                    borderRadius: BorderRadius.circular(5),
                  ),
                  child: Icon(
                    Icons.upload_file,
                    size: 70.sp(context),
                    color: Colors.white,
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  void pickFile() async {
    String filePath = await Picker.pickFile();
    String fileName = basename(filePath);
    setState(() {
      loading = true;
    });
    PDFDoc doc = await PDFDoc.fromPath(filePath);
    Get.to(
      NewRequestScreen(
        filePath: filePath,
        pagesNumber: doc.length,
        bookName: fileName.split('.').first,
      ),
    );
    setState(() {
      loading = false;
    });
  }
}
