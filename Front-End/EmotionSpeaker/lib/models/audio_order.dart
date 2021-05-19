import 'dart:convert';

import 'package:flutter/foundation.dart';

class AudioOrder {
  String id;
  String title;
  List<String> text;
  int startPage;
  int endPage;
  bool cloned;
  String audioLink;
  List<String> charactersNames;
  Map<String, dynamic> charactersVoices = {};
  String status;
  AudioOrder({
    this.id,
    this.title,
    this.text,
    this.startPage,
    this.endPage,
    this.cloned,
    this.audioLink,
    this.status,
    this.charactersNames,
  });

  AudioOrder copyWith({
    String id,
    String title,
    List<String> text,
    int startPage,
    int endPage,
    bool cloned,
    String audioLink,
    List<String> charactersNames,
  }) {
    return AudioOrder(
      id: id ?? this.id,
      title: title ?? this.title,
      text: text ?? this.text,
      startPage: startPage ?? this.startPage,
      endPage: endPage ?? this.endPage,
      cloned: cloned ?? this.cloned,
      audioLink: audioLink ?? this.audioLink,
      charactersNames: charactersNames ?? this.charactersNames,
    );
  }

  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'title': title,
      'text': text,
      'startPage': startPage,
      'endPage': endPage,
      'cloned': cloned,
      'audioLink': audioLink,
      'charactersNames': charactersNames,
    };
  }

  factory AudioOrder.fromMap(Map<String, dynamic> map) {
    return AudioOrder(
      id: map['id'],
      title: map['title'],
      text: List<String>.from(map['text']),
      startPage: map['startPage'],
      endPage: map['endPage'],
      cloned: map['cloned'],
      audioLink: map['audioLink'],
      charactersNames: map['charactersNames'] == null
          ? []
          : List<String>.from(map['charactersNames']),
      status: map["status"] == null ? "Finished" : map["status"],
    );
  }

  String toJson() => json.encode(toMap());

  factory AudioOrder.fromJson(String source) =>
      AudioOrder.fromMap(json.decode(source));

  @override
  String toString() {
    return 'AudioOrder(id: $id, title: $title, text: $text, startPage: $startPage, endPage: $endPage, cloned: $cloned, audioLink: $audioLink, charactersNames: $charactersNames)';
  }

  @override
  bool operator ==(Object other) {
    if (identical(this, other)) return true;

    return other is AudioOrder &&
        other.id == id &&
        other.title == title &&
        listEquals(other.text, text) &&
        other.startPage == startPage &&
        other.endPage == endPage &&
        other.cloned == cloned &&
        other.audioLink == audioLink &&
        listEquals(other.charactersNames, charactersNames);
  }

  @override
  int get hashCode {
    return id.hashCode ^
        title.hashCode ^
        text.hashCode ^
        startPage.hashCode ^
        endPage.hashCode ^
        cloned.hashCode ^
        audioLink.hashCode ^
        charactersNames.hashCode;
  }
}
