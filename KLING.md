# Анимация коня в Kling AI

Сайт уже умеет показывать видео вместо фото: достаточно положить готовый `.mp4` в папку `img/` с нужным именем.
Пока файла нет, остаются фото и нарисованный Тулпар (он и так анимирован: дышит, моргает, следит за курсором).

| Файл | Где появится | Исходник для Kling |
|---|---|---|
| `img/hero.mp4` | обложка, вместо фото | `kling/hero-source.jpg` |
| `img/tulpar.mp4` | Тулпар в углу, спокойный | `kling/tulpar-source.jpg` |
| `img/tulpar-talk.mp4` | Тулпар, пока говорит | `kling/tulpar-source.jpg` |

## Как сделать

1. Откройте klingai.com → **Image to Video** («Изображение в видео»).
2. Модель — самая новая из доступных, режим **Professional**, длительность **5 с**.
3. Загрузите исходник как **начальный кадр**. Чтобы видео зацикливалось без рывка, загрузите **тот же снимок как конечный кадр** (End frame).
4. Вставьте промпт и негативный промпт ниже (на английском Kling понимает точнее).
5. Сгенерируйте 2–3 варианта и выберите тот, где конь выглядит естественно: без «плывущих» ушей и лишних ног.
6. Скачайте без водяного знака и пришлите мне — я сожму видео для сайта, приведу цвет к палитре и проверю, что оно зацикливается.

**Негативный промпт (для всех трёх):**
```
camera movement, zoom, pan, shaky camera, morphing, distorted anatomy, extra ears, extra legs, melting, text, watermark, flicker
```

### 1. Обложка — `hero.mp4`
```
Static locked-off camera. A black horse stands on a high mountain plateau; its long mane and forelock flutter gently in the wind, the horse slowly blinks and twitches one ear. Grass sways softly. The distant snowy peak stays still. Calm, natural light, photorealistic, subtle motion, seamless loop.
```

### 2. Тулпар спокойный — `tulpar.mp4`
```
Static camera, close-up profile of a black horse. The horse breathes calmly, blinks, flicks its ears and slightly turns its head toward the camera, then back. The mane moves in a light breeze. Photorealistic, subtle, seamless loop.
```

### 3. Тулпар говорит — `tulpar-talk.mp4`
```
Static camera, close-up profile of a black horse that looks like it is talking: it softly moves its lips and muzzle as if speaking, nods its head a little, ears forward, friendly expression. Photorealistic, natural horse anatomy, seamless loop.
```

## Советы
- Чем спокойнее движение в промпте, тем реалистичнее результат: лошади в Kling лучше всего получаются с «тихими» действиями — дыхание, уши, грива, моргание.
- Для Тулпара важнее всего спокойная версия; говорящая — приятный бонус. Если её не будет, на сайте при разговоре просто продолжит играть спокойное видео.
- Если видео не нравится — удалите файл из `img/`, и сайт вернётся к фото и нарисованному Тулпару.
