import 'package:EmotionSpeaker/common_widgets/hidden_menu/controllers/simple_hidden_drawer_controller.dart';
import 'package:EmotionSpeaker/common_widgets/hidden_menu/menu/hidden_menu_widget.dart';
import 'package:EmotionSpeaker/common_widgets/hidden_menu/model/item_hidden_menu.dart';
import 'package:EmotionSpeaker/common_widgets/hidden_menu/simple_hidden_drawer/animated_drawer_content.dart';
import 'package:flutter/material.dart';

class HiddenMenu extends StatefulWidget {
  /// Decocator that allows us to add backgroud in the menu(img)
  final DecorationImage background;

  /// that allows us to add shadow above menu items
  final bool enableShadowitemsMenu;

  /// that allows us to add backgroud in the menu(color)
  final Color backgroundColorMenu;

  /// Items of the menu
  final List<ItemHiddenMenu> items;

  /// Callback to recive item selected for user
  final Function(int) selectedListern;

  /// position to set initial item selected in menu
  final int initPositionSelected;

  final TypeOpen typeOpen;

  HiddenMenu(
      {Key key,
      this.background,
      this.items,
      this.selectedListern,
      this.initPositionSelected,
      this.backgroundColorMenu,
      this.enableShadowitemsMenu = false,
      this.typeOpen = TypeOpen.FROM_LEFT})
      : super(key: key);

  @override
  _HiddenMenuState createState() => _HiddenMenuState();
}

class _HiddenMenuState extends State<HiddenMenu> {
  int _indexSelected;
  SimpleHiddenDrawerController controller;

  @override
  void initState() {
    _indexSelected = widget.initPositionSelected;
    super.initState();
  }

  @override
  void didChangeDependencies() {
    controller = SimpleHiddenDrawerController.of(context);
    controller.addListener(_listenerController);
    super.didChangeDependencies();
  }

  @override
  void dispose() {
    controller.removeListener(_listenerController);
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        decoration: BoxDecoration(
          image: widget.background,
          color: widget.backgroundColorMenu,
        ),
        child: Center(
          child: Container(
            padding: EdgeInsets.only(top: 40.0, bottom: 40.0),
            decoration: BoxDecoration(
              boxShadow: widget.enableShadowitemsMenu
                  ? [
                      new BoxShadow(
                        color: const Color(0x44000000),
                        offset: const Offset(0.0, 5.0),
                        blurRadius: 50.0,
                        spreadRadius: 30.0,
                      ),
                    ]
                  : [],
            ),
            child: ListView.builder(
              physics: NeverScrollableScrollPhysics(),
              shrinkWrap: true,
              padding: EdgeInsets.all(0.0),
              itemCount: widget.items.length,
              itemBuilder: (context, index) {
                return HiddenMenuWidget(
                  name: widget.items[index].name,
                  selected: index == _indexSelected,
                  colorLineSelected: widget.items[index].colorLineSelected,
                  baseStyle: widget.items[index].baseStyle,
                  selectedStyle: widget.items[index].selectedStyle,
                  typeOpen: widget.typeOpen,
                  onTap: () {
                    if (widget.items[index].onTap != null) {
                      widget.items[index].onTap();
                    }
                    controller.setSelectedMenuPosition(index);
                  },
                );
              },
            ),
          ),
        ),
      ),
    );
  }

  void _listenerController() {
    setState(() {
      _indexSelected = controller.position;
    });
  }
}