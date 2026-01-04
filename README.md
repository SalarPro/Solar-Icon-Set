<img src="src/banner.png">

# Solar Icon Set - free giant icon pack as big as Solar System!

> 🍴 **This is a fork of [480-Design/Solar-Icon-Set](https://github.com/480-Design/Solar-Icon-Set)** with an added icon gallery browser.

## What is this?

Solar is a large icon library consisting of pictograms that are modern in style. Their peculiarity lies in the fact that they have corner smoothing raised up to 100%. And because of this interesting feature the icons look quite unique and catchy. All icons are made inside of Figma using special grid which makes them perfectly balanced and adjusted in relation to each other. 

## What's inside?

✨ 7479 fully customisable sexy icons

✨ 37 popular categories

✨ 6 icon styles: Linear, Line Duotone, Bold, Bold Duotone, Broken, Outline

✨ Icon Grid with variations 

✨ Free premium content

✨ Much of love from 480 Design and from creator of those icons! 

---

## 🖼️ Icon Gallery Browser

This fork includes a web-based icon gallery that lets you:

- **Search** icons by name instantly
- **Filter** by icon type (Bold, Linear, Broken, etc.) and category
- **Copy** icons in three formats:
  - **CamelCase** - e.g., `solarBrokenAstronomyBlackHole2`
  - **Path** - e.g., `icons/solar/broken/astronomy/black_hole_2.svg`
  - **SVG Code** - the raw SVG markup
- **Dark/Light theme** toggle

### How to Use

#### 1. Generate the Icon Manifest

First, generate the `manifest.json` file that indexes all icons:

```bash
node build-manifest.js
```

This scans the `icons/solar/` directory and creates a manifest with all icon paths, types, and categories.

#### 2. Start a Local Server

The gallery needs to be served from a web server (not opened directly as a file). You can use any of these methods:

**Using Python:**
```bash
python3 -m http.server 8080
```

**Using Node.js (with http-server):**
```bash
npx http-server -p 8080
```

**Using PHP:**
```bash
php -S localhost:8080
```

#### 3. Open the Gallery

Open your browser and navigate to:
```
http://localhost:8080
```

### File Structure

```
├── index.html          # Icon gallery web page
├── build-manifest.js   # Script to generate icon manifest
├── manifest.json       # Generated icon index (after running build script)
└── icons/
    └── solar/
        ├── bold/
        ├── bold_duotone/
        ├── broken/
        ├── line_duotone/
        ├── linear/
        └── outline/
```

---

We would absolutely love you using this pack in Your projects! Share these cool icons with friends or colleagues, drop a like, leave comments down below and follow is for more cool freebie stuff! ❤️‍🔥

## Original Repository
* [GitHub - 480-Design/Solar-Icon-Set](https://github.com/480-Design/Solar-Icon-Set)

## We are also in the
* [Figma](https://www.figma.com/@480design)
* [Telegram](https://t.me/Design480)

## Contact author
t.me/tierohnenation

