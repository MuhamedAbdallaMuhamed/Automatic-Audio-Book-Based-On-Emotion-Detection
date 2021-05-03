import 'package:EmotionSpeaker/api/dio_api.dart';
import 'package:EmotionSpeaker/models/result.dart';
import 'package:EmotionSpeaker/models/audio_order.dart';
import 'package:EmotionSpeaker/constants/user_base.dart';
import 'package:EmotionSpeaker/constants/keys.dart';
import 'package:dio/dio.dart';

class AudioOrderServices {
  DioClient dio = DioClient();
  Future<Result> addAudioOrder(
      {AudioOrder audioOrder, String accessToken}) async {
    Response response;
    try {
      print(accessToken);
      response = await dio.post(
        uri: UserBase.Url + UserBase.AudioOrder,
        data: audioOrder.toJson(),
        options: Options(
          headers: {
            Keys.Authorization: Keys.Bearer + accessToken,
          },
        ),
      );
      print(response.data);
      if (response.statusCode == 200) {
        return Result.success(response.data['message']);
      } else {
        print(response.statusCode);
        String resultMessage = response.data['message'];
        return Result.error(resultMessage);
      }
    } catch (e) {
      return Result.error(response.data['message']);
    }
  }
}
