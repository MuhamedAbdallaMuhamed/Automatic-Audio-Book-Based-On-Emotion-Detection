import 'package:EmotionSpeaker/models/user.dart';
import 'package:get/state_manager.dart';

import 'package:EmotionSpeaker/repository/user_repository.dart';
import 'package:EmotionSpeaker/models/result.dart';

class UserController extends GetxController {
  String accessToken;
  String refreshToken;
  UserRepository userRepository = UserRepository();
  Future<Result> userLogin({User user}) async {
    Result result = await userRepository.userLogin(user: user);
    if (result is SuccessResult) {
      List list = result.getSuccessData();
      accessToken = list[0];
      refreshToken = list[1];
    }
  }
}
