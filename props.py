props = {
  "icon": "IconSource",
  "mode": "IconButtonMode",
  "iconColor": "string",
  "containerColor": "string",
  "selected": "boolean",
  "size": "number",
  "disabled": "boolean",
  "accessibilityLabel": "string",
  "onPress": "(e: GestureResponderEvent) => void",
  "style": "StyleProp<ViewStyle>",
  "ref": "React.RefObject<TouchableWithoutFeedback>",
  "theme": "Theme"
}

for key, value in props.items():
    print(f"### {key} \nType: `{value}`","\n")
