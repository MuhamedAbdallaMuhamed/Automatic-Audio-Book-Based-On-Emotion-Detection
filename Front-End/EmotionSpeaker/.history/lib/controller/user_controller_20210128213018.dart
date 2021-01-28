import 'package:EmotionSpeaker/models/user.dart';
import 'package:get/state_manager.dart';

import 'package:EmotionSpeaker/repository/user_repository.dart';
import 'package:EmotionSpeaker/models/result.dart';

class UserController extends GetxController {
  UserRepository userRepository = UserRepository();
  Future<Result> userLogin({User user}) async {}
}
