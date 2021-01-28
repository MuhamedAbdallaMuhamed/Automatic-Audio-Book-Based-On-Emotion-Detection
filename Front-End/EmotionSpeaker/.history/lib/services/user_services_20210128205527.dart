import 'package:EmotionSpeaker/api/dio_api.dart';
import 'package:EmotionSpeaker/models/result.dart';
import 'package:EmotionSpeaker/models/user.dart';
import 'package:dio/dio.dart';

class UserServices {
  DioClient dio = DioClient();
  Result userLogin(User user) async {
    Response response = await dio.post();
  }
}
