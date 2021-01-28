import 'package:EmotionSpeaker/api/dio_api.dart';
import 'package:EmotionSpeaker/constants/user_base.dart';
import 'package:EmotionSpeaker/models/result.dart';
import 'package:EmotionSpeaker/models/user.dart';
import 'package:dio/dio.dart';

class UserServices {
  DioClient dio = DioClient();
  Future<Result> userLogin(User user) async {
    Response response = await dio.post(
      uri: UserBase.Url + UserBase.Login,
      data: user.toJson(),
    );
    if (response.statusCode == 200) {
      String accessToken = response.data['access_token'];
      String refreshToken = response.data['refresh_token'];
      return Result.success([accessToken, refreshToken]);
    } else {
      String resultMessage = response.data['message'];
      return Result.error(resultMessage);
    }
  }
}
