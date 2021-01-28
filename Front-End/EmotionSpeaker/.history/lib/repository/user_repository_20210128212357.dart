import 'package:EmotionSpeaker/models/user.dart';
import 'package:EmotionSpeaker/services/user_services.dart';
import 'package:EmotionSpeaker/models/result.dart';

class UserRepository {
  UserServices userServices = UserServices();
  Future<Result> userLogin({User user}) async {
    try {
      Result result = userServices.userLogin(user: user);
    } catch (e) {
      return Result.error('Application Error');
    }
  }
}
