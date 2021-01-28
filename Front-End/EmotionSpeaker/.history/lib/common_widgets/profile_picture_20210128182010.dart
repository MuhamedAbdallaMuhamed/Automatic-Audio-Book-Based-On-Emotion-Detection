import 'package:flutter/material.dart';
import 'package:Enaba/utils/sizing_extension.dart';
import 'package:Enaba/utils/picker.dart';
import 'dart:io';
import 'package:meet_network_image/meet_network_image.dart';

// ignore: must_be_immutable
class ProfilePicture extends StatefulWidget {
  ProfilePicture({
    Key key,
    @required this.fileFun,
    this.link,
    this.edit = false,
  }) : super(key: key);
  final Function(File) fileFun;
  final String link;
  final bool edit;
  @override
  _ProfilePictureState createState() => _ProfilePictureState();
}

class _ProfilePictureState extends State<ProfilePicture> {
  File _file;
  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: ontap,
      child: Center(
        child: Stack(
          alignment: FractionalOffset.bottomRight,
          children: [
            Container(
              width: 128.wp(context),
              height: 128.wp(context),
              decoration: BoxDecoration(
                color: Colors.grey.shade300,
                shape: BoxShape.circle,
                border: Border.all(
                  color: Colors.white,
                  width: 1,
                ),
                boxShadow: [
                  BoxShadow(
                    color: Colors.black38,
                    blurRadius: 1,
                  ),
                ],
                image: _file == null
                    ? null
                    : DecorationImage(
                        fit: BoxFit.fill,
                        image: FileImage(
                          _file,
                        ),
                      ),
              ),
              child: _file == null
                  ? widget.link == null
                      ? Center(
                          child: Icon(
                            Icons.person,
                            color: Colors.grey,
                            size: 100.sp(context),
                          ),
                        )
                      : ClipRRect(
                          borderRadius: BorderRadius.circular(180),
                          child: MeetNetworkImage(
                            imageUrl: widget.link,
                            loadingBuilder: (context) => Center(
                              child: CircularProgressIndicator(),
                            ),
                            errorBuilder: (context, e) => Center(
                              child: Text('Error appear!'),
                            ),
                          ),
                        )
                  : null,
            ),
            if (!widget.edit)
              CircleAvatar(
                backgroundColor: Colors.white,
                radius: 20.wp(context),
                child: IconButton(
                  icon: Icon(
                    Icons.camera_alt,
                    color: Colors.black,
                  ),
                  onPressed: ontap,
                ),
              ),
          ],
        ),
      ),
    );
  }

  void ontap() async {
    _file = await Picker.pickImage();
    _file = await Picker.cropImage(_file);
    widget.fileFun(_file);
    setState(() {});
  }
}
