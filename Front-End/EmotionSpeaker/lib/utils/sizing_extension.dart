import 'package:flutter/material.dart';

int hp, wp, sp, heightPercentage, widthPercentage;

extension SizingExtension on num {
  ///Reduce scale percentage to 35% only
  static const double scaleUpReductionFactor = .35; //35%
  static const double scaleDownReductionFactor = 1; //100%

  ///The reference screen is 5 inches android phone (360*640 LogicalPixels)
  static const Size referenceScreenSize = Size(375, 812);

  num sp(BuildContext context) => this._calculateWP(context);

  num widthPercentage(BuildContext context) =>
      this._calculateWidthPercentage(context);

  num heightPercentage(BuildContext context) =>
      this._calculateHeightPercentage(context);

  num wp(BuildContext context) => this._calculateWP(context);

  num hp(BuildContext context) => this._calculateHP(context);

  num _calculateWidthPercentage(BuildContext context) {
    double screenWidth = MediaQuery.of(context).size.width;
    return this / 100 * screenWidth;
  }

  num _calculateHeightPercentage(BuildContext context) {
    double screenHeight = MediaQuery.of(context).size.height;
    return this / 100 * screenHeight;
  }

  num _calculateWP(BuildContext context) {
    double screenWidth = MediaQuery.of(context).size.width;
    double refScreenWidth = _getRefScreenWidth(context);
    double scaleReductionFactor = screenWidth > refScreenWidth
        ? scaleUpReductionFactor
        : scaleDownReductionFactor;
    return (this *
            (1 + (screenWidth / refScreenWidth - 1) * scaleReductionFactor))
        .toDouble();
  }

  ///if current [screenHeight] is less than the [referenceScreenSize.height] ->
  ///reduce the height by the same ratio percentage between them (scaleReductionFactor = 100%).
  ///but if [screenHeight] is greater than ReferenceScreenHeight [referenceScreenSize.height] ->
  ///increase the height by only scaleReductionFactor(35%) of the ratio percentage between them.
  num _calculateHP(BuildContext context) {
    double screenHeight = MediaQuery.of(context).size.height;
    double refScreenHeight = _getRefScreenHeight(context);
    double scaleReductionFactor = screenHeight > refScreenHeight
        ? scaleUpReductionFactor
        : scaleDownReductionFactor;
    return (this *
            (1 + (screenHeight / refScreenHeight - 1) * scaleReductionFactor))
        .toDouble();
  }

  double _getRefScreenWidth(BuildContext context) {
    Orientation orientation = MediaQuery.of(context).orientation;
    return orientation == Orientation.portrait
        ? referenceScreenSize.shortestSide
        : referenceScreenSize.longestSide;
  }

  double _getRefScreenHeight(BuildContext context) {
    Orientation orientation = MediaQuery.of(context).orientation;
    return orientation == Orientation.portrait
        ? referenceScreenSize.longestSide
        : referenceScreenSize.shortestSide;
  }
}
