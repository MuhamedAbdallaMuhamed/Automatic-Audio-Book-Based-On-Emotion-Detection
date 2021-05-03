import 'package:EmotionSpeaker/models/audio_order.dart';
import 'package:EmotionSpeaker/models/result.dart';
import 'package:EmotionSpeaker/services/audio_order_services.dart';

class AudioOrderRepository {
  AudioOrderServices audioOrderServices = AudioOrderServices();
  Future<Result> addAudioOrder(
      {AudioOrder audioOrder, String accessToken}) async {
    try {
      Result result = await audioOrderServices.addAudioOrder(
        audioOrder: audioOrder,
        accessToken: accessToken,
      );
      return result;
    } catch (e) {
      return Result.error('Application Error');
    }
  }
  Future<Result> getAllAudioOrder(
      {String accessToken}) async {
    try {
      Result result = await audioOrderServices.getAllOrders(
        accessToken: accessToken,
      );
      return result;
    } catch (e) {
      return Result.error('Application Error');
    }
  }
}
