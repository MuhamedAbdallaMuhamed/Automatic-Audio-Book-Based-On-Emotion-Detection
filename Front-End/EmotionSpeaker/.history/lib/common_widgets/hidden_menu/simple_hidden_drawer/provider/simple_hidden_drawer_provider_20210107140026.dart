import 'package:EmotionSpeaker/common_widgets/hidden_menu/controllers/simple_hidden_drawer_controller.dart';
import 'package:flutter/material.dart';

class MyProvider extends InheritedWidget {
  final SimpleHiddenDrawerController controller;

  MyProvider({
    Key key,
    @required this.controller,
    Widget child,
  }) : super(key: key, child: child);

  @override
  bool updateShouldNotify(InheritedWidget oldWidget) => true;
}
