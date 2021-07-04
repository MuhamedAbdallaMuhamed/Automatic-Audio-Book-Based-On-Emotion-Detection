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

  Future<Result> getAllOrders({String accessToken}) async {
    Response response;
    try {
      print(accessToken);
      response = await dio.get(
        uri: UserBase.Url + UserBase.AudioOrder,
        options: Options(
          headers: {
            Keys.Authorization: Keys.Bearer + accessToken,
          },
        ),
      );
      if (response.statusCode == 200) {
        List<AudioOrder> orders = [];
        var ordersList = response.data['orders'] as List ?? [];
        for (int i = 0; i < ordersList.length; i++) {
          print("HEREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE");
          print(ordersList[i]);
          final order = AudioOrder.fromMap(ordersList[i]);
          orders.add(order);
        }
        return Result.success(orders);
      } else {
        print(response.statusCode);
        String resultMessage = response.data['message'];
        return Result.error(resultMessage);
      }
    } catch (e) {
      return Result.error(response.data['message']);
    }
  }

  Future<Result> sendCharacterVoices({
    String accessToken,
    AudioOrder audioOrder,
  }) async {
    Response response;
    try {
      print(accessToken);
      FormData formData = FormData();
      print(audioOrder.charactersVoices);
      /*audioOrder.charactersVoices.forEach((character, voice) async {
        MultipartFile file = await MultipartFile.fromFile(voice);
        formData.files.add(MapEntry(character, file));
      });*/
      for (var k in audioOrder.charactersVoices.keys) {
        MultipartFile file =
            await MultipartFile.fromFile(audioOrder.charactersVoices[k]);
        formData.files.add(MapEntry(k, file));
      }
      formData.fields.add(MapEntry("audio_id", audioOrder.id));
      response = await dio.put(
        uri: UserBase.Url + UserBase.AudioOrder,
        data: formData,
        options: Options(
          headers: {
            Keys.Authorization: Keys.Bearer + accessToken,
          },
        ),
      );
      String resultMessage = response.data['message'];
      if (response.statusCode == 200) {
        return Result.success(resultMessage);
      } else {
        print(response.statusCode);
        return Result.error(resultMessage);
      }
    } catch (e) {
      return Result.error(response.data['message']);
    }
  }
}
