```
Try to find way using component in scss module.
```

---


**Me:**
How to use style written in another scss module in react application?

---

**ChatGPT:**
To use styles written in another SCSS module in a React application, you can follow these steps:
<li>Import the SCSS module containing the styles you want to use:</li><br/>

```scss
@import 'path/to/other/module';
```
<li>Apply the styles to the appropriate components in your React application:</li><br/>

```jsx
import React from 'react';
import styles from 'path/to/other/module';

const MyComponent = () => {
  return (
    <div className={styles.myClassName}>
      {/* content */}
    </div>
  );
};

export default MyComponent;
```
Note that the imported styles are accessed as an object, with the class names as properties.
<li>Make sure that your React application is set up to process SCSS files. You can use a tool like Webpack with the <code>sass-loader</code> and <code>css-loader</code> to do this.</li><br/>

```javascript
{
  test: /\.scss$/,
  use: [
    'style-loader',
    'css-loader',
    'sass-loader'
  ]
}
```
This configuration will process your SCSS files and create CSS files that can be included in your React application. The <code>style-loader</code> will add the CSS to the DOM, and the <code>css-loader</code> will enable the use of <code>import</code> statements for your styles.
With these steps, you should be able to use styles from other SCSS modules in your React application.

---

**Me:**
but how can i use imported class style in scss module itself for complex selectors

---

**ChatGPT:**
To use an imported class style in a complex selector in an SCSS module, you can use the <code>@extend</code> directive. Here's an example:
Suppose you have a SCSS module named <code>button.module.scss</code>, and you want to define a complex selector for a button with a red background color, but you also want to reuse the styles from another SCSS module named <code>base.module.scss</code>. Here's how you can do it:
```scss
@import 'path/to/base.module.scss';

.button {
  // Use styles from the base module
  @extend .base-style;

  // Define additional styles for the button
  background-color: red;

  // Define a complex selector using the imported class and the new styles
  &.disabled {
    opacity: 0.5;
  }
}
```
In this example, the <code>@extend</code> directive is used to inherit the styles from the <code>.base-style</code> class defined in the <code>base.module.scss</code> module. Then, the <code>background-color</code> property is defined to give the button a red background color. Finally, a complex selector is defined for a disabled button by combining the <code>.button</code> class and the <code>.disabled</code> class.
Note that when you use <code>@extend</code>, the styles from the base class are included in the CSS output, so it's important to make sure you're not duplicating styles unnecessarily.

---

**Me:**
i need classname from another module to compose selector name rather than use its styles part

---

**ChatGPT:**
If you need to use a class name from another SCSS module as part of a complex selector, but you don't want to inherit the styles from that class, you can use string interpolation to create the selector name.
Here's an example:
Suppose you have a SCSS module named <code>button.module.scss</code>, and you want to define a complex selector for a button with a red background color that also includes a class name from another module named <code>utils.module.scss</code>. Here's how you can do it:
```scss
@import 'path/to/utils.module.scss';

$utils-class: 'some-class';

.button.#{$utils-class} {
  // Define styles for the button with the utils class
  background-color: red;
}
```
In this example, the <code>$utils-class</code> variable is set to the name of the class you want to include in the selector. Then, the <code>#{$utils-class}</code> syntax is used within the selector to interpolate the value of the variable and create the selector name.
Note that in this example, the styles from the <code>some-class</code> class defined in the <code>utils.module.scss</code> module are not inherited by the <code>.button</code> class. Instead, the <code>some-class</code> name is used only to compose the selector name.

---

**Me:**
idk where exactly problem is, but thats not working. I have parent component in react app and child component, which stored in parent folder. I'm trying to import child module styles in parent module and technically it seems to work, no program errors at least. But when i try to use selector &:hover > {child class name}, styles does not apply for child on parent element hovering

---

**ChatGPT:**
It sounds like you're trying to use a child class name in a parent SCSS module, but the styles are not being applied when you use a hover selector.
One possible reason for this is that the child styles are scoped to the child component and are not accessible from the parent module. In other words, the child styles may be encapsulated within the child component and not available for use in other components.
To solve this problem, you can try a few different approaches:
<li>Pass the styles from the child component to the parent component using props. In the child component, you can define the styles you want to use and pass them to the parent component as a prop. Then, in the parent component, you can apply the styles using the prop value.</li><li>Define the styles in a shared SCSS module that can be imported by both the parent and child components. This will make the styles accessible from both components, and you can use them in the parent module as needed.</li><li>Use a CSS-in-JS solution like styled-components or emotion to define the styles in the child component and pass them to the parent component as a prop. This will allow you to define the styles in the same file as the child component and make them available for use in the parent component.</li>
If none of these solutions work, it may be helpful to provide more information about the specific code you're using and any error messages you're seeing.

---

**Me:**
is there a way how can i see resulted styles in react app without building?

---

**ChatGPT:**
Yes, there are a few different ways to see the resulting styles in a React app without building the app:
<li>Use a browser extension like "Stylebot" (for Chrome) or "Stylish" (for Firefox) to inspect and modify the styles on a live webpage. These extensions allow you to modify the CSS styles for any webpage you're viewing, including a local React app running in your browser.</li><li>Use the browser's built-in developer tools to inspect and modify the styles on a live webpage. Most modern browsers include a set of developer tools that allow you to inspect the HTML and CSS of a webpage, including a local React app running in your browser.</li><li>Use a third-party tool like "CSS Scan" or "CSS Peeper" to inspect and export the styles on a live webpage. These tools allow you to inspect the CSS styles for any webpage you're viewing, including a local React app running in your browser, and export the styles as a CSS file.</li>
Note that these solutions allow you to see the final styles applied to the rendered HTML, but they may not show the full picture if the styles are being generated dynamically in response to user interactions or other events. In these cases, it may be necessary to examine the source code and/or debug the application to see the full picture of how styles are being applied.

---

**Me:**
how to see full picture if styles generated dynamically

---

**ChatGPT:**
If the styles are being generated dynamically in response to user interactions or other events, it may be necessary to examine the source code and/or debug the application to see the full picture of how styles are being applied.
Here are some steps you can follow to debug dynamic styles in a React app:
<li>Use the browser's developer tools to inspect the HTML and CSS of the page. You can use the "Elements" tab to view the HTML source code and the "Styles" tab to view the CSS styles applied to the elements.</li><li>Look for elements or styles that are being added or modified in response to user interactions or other events. These may be added or modified using JavaScript code, so you may need to look for code that is executed in response to an event listener or other trigger.</li><li>Use the debugger in the browser's developer tools to step through the JavaScript code and see how the styles are being generated. You can set breakpoints in the code to pause execution at a specific point and examine the variables and other data being used to generate the styles.</li><li>Use console.log statements in the JavaScript code to log variables and other data being used to generate the styles. This can help you understand how the styles are being generated and identify any errors or issues in the code.</li><li>If necessary, consult the documentation or other resources for any libraries or frameworks being used in the app. These resources may provide additional guidance or troubleshooting tips for working with dynamic styles.</li>
By following these steps, you should be able to gain a better understanding of how the styles are being generated and identify any issues or errors in the code.

---

**Me:**
you give me advice to pass style to the parent component, but i want to use it directly in scss module, so how can i achive this?

---

**ChatGPT:**
If you want to use the child component's styles directly in a parent SCSS module, you can use the <code>@import</code> directive to import the child SCSS module into the parent module. Then, you can use the child class names in the parent module's selectors to apply the child component's styles.
Here's an example:
In the child component's SCSS module (<code>child.scss</code>), define the styles you want to use:
```scss
.child {
  background-color: red;
  color: white;
}
```
In the parent component's SCSS module (<code>parent.scss</code>), import the child module and use its class name in a selector:
```scss
@import "./child.scss";

.parent:hover > .child {
  background-color: blue;
}
```
In this example, the <code>@import</code> directive is used to import the <code>child.scss</code> module into the <code>parent.scss</code> module. Then, in the <code>parent.scss</code> module's selector, the <code>.child</code> class name is used to apply the child component's styles to the parent component when it is hovered over.
Note that in order for this to work, the child component's styles must not be scoped to the child component using a CSS module or similar technique. If the styles are scoped in this way, they may not be accessible from the parent SCSS module.

---

**Me:**
can i use react component name in scss module as tag name for selector?

---

**ChatGPT:**
Yes, you can use a React component name as a tag name in a SCSS module's selector.
Assuming you have a React component named <code>MyComponent</code>, you can use it as a tag name in a SCSS module like this:
```scss
MyComponent {
  /* Styles for MyComponent */
}
```
This will apply the styles to any instances of the <code>MyComponent</code> component that are rendered in the HTML. Note that this will only work if the component is rendered with that exact tag name (e.g. <code>&lt;MyComponent /&gt;</code>). If the component is rendered with a different tag name or as a functional component (e.g. <code>MyComponent()</code>), the styles will not be applied.
Additionally, note that using tag names in selectors can be less specific than using class names or other selectors, which could lead to unintended styling of other elements on the page. It's generally a good practice to use more specific selectors whenever possible to avoid unintentional side effects.

---

**Me:**
&:hover > MergeButton { // styles for component } that type of thing not working, where MergeButton is child component relative to component where this style has been defined

---

**ChatGPT:**
If <code>MergeButton</code> is a child component of the component where the hover style is defined, you should be able to target it using a child combinator (<code>&gt;</code>).
Here's an example:
```scss
.parent-component:hover > .child-component {
  /* styles for child component */
}
```
In this example, <code>parent-component</code> is the class name of the parent component, and <code>child-component</code> is the class name of the child component. The <code>&gt;</code> combinator is used to target only the direct child components of the parent component that are hovered over.
If you are still having trouble getting the style to apply, there may be an issue with the CSS specificity of your selector. Make sure that the selector you are using is more specific than any other selectors that may be affecting the same element. You can use the browser's developer tools to inspect the element and see which selectors are being applied to it, and adjust your selector accordingly.

---

**Me:**
but how can i use child component tag name rather than child component class name?

---

**ChatGPT:**
If you want to use the tag name of a child component in a parent component's SCSS module, you can use the child component's <code>displayName</code> property to reference its tag name.
Assuming the child component has a <code>displayName</code> of <code>MyChildComponent</code>, you can reference its tag name in the parent component's SCSS module like this:
```scss
.parent-component:hover > MyChildComponent {
  /* styles for child component */
}
```
In this example, <code>parent-component</code> is the class name of the parent component, and <code>MyChildComponent</code> is the tag name of the child component. The <code>&gt;</code> combinator is used to target only the direct child components of the parent component that are hovered over.
Note that the <code>displayName</code> property is not required for a React component to function, but it can be helpful for debugging and other purposes. If the child component does not have a <code>displayName</code> property set, you can alternatively reference its tag name by using the tag name directly (e.g. <code>div</code>, <code>span</code>, etc.) or by using the class name of the component.

---

**Me:**
but would it work if i make build of the application?

---

**ChatGPT:**
Yes, referencing a child component by its tag name using the <code>displayName</code> property in a parent component's SCSS module should work even after building the application.
When you build your application, the SCSS files will be compiled into CSS, and any references to child components by their tag names will be compiled into CSS selectors that target the appropriate elements. As long as the child component is rendered with the correct tag name, the CSS selectors should be able to target it correctly.
Note that if you are using a tool like CSS Modules to scope your styles to specific components, you may need to use a different syntax to reference child components by their tag names. The syntax for doing so may depend on the specific implementation of CSS Modules that you are using, so you should consult the documentation for your chosen implementation to see how to reference child components by tag name.

---

**Me:**
thing with display name does not seemed to work. I set displayName to child component:

---

**ChatGPT:**
If setting the <code>displayName</code> property on the child component does not seem to be working for you, there may be other factors at play that are preventing the styles from being applied.
One thing to check is whether the child component is being rendered with the correct tag name. If the child component is being rendered with a different tag name than what you are targeting in the parent component's SCSS module, the styles will not be applied.
Another thing to check is whether the child component's SCSS module is being properly imported and included in your application's build process. If the child component's SCSS module is not being included in the build, the styles defined in that module will not be applied.
If you have checked both of these factors and are still having trouble getting the styles to apply, there may be an issue with the specificity of your CSS selectors or with other CSS rules that are overriding the styles you are trying to apply. You can use your browser's developer tools to inspect the element and see which styles are being applied, and adjust your CSS accordingly.

---

**Me:**
how to check if displayName is working?

---

**ChatGPT:**
If you want to check whether the <code>displayName</code> property is set correctly on a React component, you can use the browser's developer tools to inspect the component.
In Chrome, for example, you can right-click on the component and select "Inspect" to open the Elements tab. From there, you can expand the component to view its properties and check whether the <code>displayName</code> property is set to the expected value.
Alternatively, you can add some code to the child component to log the value of its <code>displayName</code> property to the console, like so:
```jsx
import React from "react";

const MyChildComponent = () => {
  console.log("MyChildComponent displayName:", MyChildComponent.displayName);
  return <div>Child component content</div>;
};

MyChildComponent.displayName = "MyChildComponent";

export default MyChildComponent;
```
When you render the child component in your parent component, the console should output the value of the <code>displayName</code> property, allowing you to confirm whether it is set correctly.

---

**Me:**
in console log i see correct displayName, but i do not see anything in element tab

---

**ChatGPT:**
If you see the correct <code>displayName</code> value in the console log, but it does not show up in the Elements tab of your browser's developer tools, it may be because the <code>displayName</code> property is not a standard HTML attribute and is therefore not visible in the Elements tab.
To verify that the <code>displayName</code> property is actually being used in your CSS selectors, you can inspect the compiled CSS in your browser's developer tools. Look for the CSS rules that reference the child component, and check whether they include the tag name that corresponds to the <code>displayName</code> value. For example, if the <code>displayName</code> value is set to <code>MyChildComponent</code>, you should see CSS rules that look like this:
```css
.my-parent-component MyChildComponent {
  /* styles */
}
```
If you see these CSS rules and they are not being applied, there may be an issue with your CSS specificity or with other CSS rules that are overriding your styles. You can use your browser's developer tools to debug these issues and adjust your CSS accordingly.

---

**Me:**
thas not working when i set (& - parent component reference) &:hover > ChildComponent, but when i use &:hover > div:first-child it workds

---

**ChatGPT:**
If using <code>&amp;:hover &gt; ChildComponent</code> does not work, but <code>&amp;:hover &gt; div:first-child</code> does work, it could be because the <code>ChildComponent</code> is not being rendered as a direct child of the parent component, but is wrapped in an additional <code>div</code> or other element.
When you use <code>&amp;:hover &gt; div:first-child</code>, you are targeting the first child element of the parent component, regardless of its tag name. This will match any element that is the first child of the parent component, whether it is a <code>div</code>, <code>span</code>, or any other tag.
On the other hand, when you use <code>&amp;:hover &gt; ChildComponent</code>, you are targeting only the direct child elements of the parent component that are of the <code>ChildComponent</code> type. If the <code>ChildComponent</code> is not being rendered directly as a child of the parent component, this selector will not match anything.
To target the <code>ChildComponent</code> regardless of its position in the component tree, you can use the <code>*</code> universal selector instead of the direct child selector <code>&gt;</code>:
```scss
&:hover > * {
  // styles for direct child elements
}

&:hover > ChildComponent {
  // styles for direct ChildComponent children
}
```
This will match any direct child element of the parent component, regardless of its tag name or component type.

---

**Me:**
yes it is wrapped in additional div in fact & - .ParentClass .WrapperChildDivClass but what can i do to make displayName works in scss file?

---

**ChatGPT:**
If your child component is wrapped in an additional <code>div</code>, you can still use the <code>displayName</code> property to target it in your SCSS file. You will just need to adjust your selector to account for the extra <code>div</code> wrapper.
Assuming your <code>WrapperChildDivClass</code> is unique to your child component, you can use it in your selector like this:
```scss
.ParentClass .WrapperChildDivClass:hover > ChildComponent {
  // styles for child component
}
```
Here, we are using a descendant selector to target the <code>ChildComponent</code> inside the <code>WrapperChildDivClass</code>. This will work as long as the <code>WrapperChildDivClass</code> is unique to your child component, and is not used for any other elements in your parent component.
As for using the <code>displayName</code> property in your SCSS file, you can use it in the same way as before. Just make sure that you are passing the correct <code>displayName</code> value to your child component, and that it is being set correctly in the child component's <code>props</code> object.
If you are still having issues with the <code>displayName</code> property, you can try logging it to the console in your child component to verify that it is being set correctly. If it is, then the issue may be with your selector, and you may need to adjust it to target the correct element.

---

**Me:**
but what if do not pass it through props but define displayName in child component itself?

---

**ChatGPT:**
If you define the <code>displayName</code> property in the child component itself, you can still use it to target the component in your SCSS file.
Here's an example of how you can define the <code>displayName</code> property in a child component:
```jsx
const ChildComponent = () => {
  // component logic here

  return (
    // JSX markup here
  );
}

ChildComponent.displayName = 'ChildComponent';
```
Here, we are defining the <code>displayName</code> property directly on the <code>ChildComponent</code> function. This property will be available on the <code>ChildComponent</code> object, and can be accessed by other parts of your code, including your SCSS file.
To target the <code>ChildComponent</code> using its <code>displayName</code>, you can use a class selector that matches the <code>displayName</code> value:
```scss
.ParentClass .WrapperChildDivClass:hover > .ChildComponent {
  // styles for child component
}
```
Here, we are using a class selector <code>.ChildComponent</code> to target the child component using its <code>displayName</code> value.
Note that the class selector matches the <code>displayName</code> value exactly, so make sure to define the <code>displayName</code> property with the correct capitalization and spelling.

---

**Me:**
that simply does not work, i define this style in Parent.module.scss, so all classes there receive are modified to something like Parent_ClassName_hash, so that thing with displayName does not seem to work

---

**ChatGPT:**
If your styles are being modified by SCSS, such as by adding hashes to class names, then using the <code>displayName</code> property to target components in your SCSS file may not work as expected.
In this case, you may need to use a different approach to target your child components. One approach is to use the class names generated by SCSS to target your child components.
For example, if your child component has a class name of <code>ChildComponent</code>, and your parent component has a class name of <code>Parent</code>, you can target the child component like this:
```scss
.Parent_ClassName:hover .ChildComponent {
  // styles for child component
}
```
Here, we are using a descendant selector to target the <code>ChildComponent</code> inside the <code>Parent</code> component. The class names for both the parent and child components have been modified by SCSS, so we use the modified class names to target them.
If you have multiple instances of the <code>ChildComponent</code> inside the <code>Parent</code> component, you can use a more specific selector to target a specific instance. For example, if the <code>ChildComponent</code> has an additional class name of <code>child1</code>, you can target it like this:
```scss
.Parent_ClassName:hover .ChildComponent.child1 {
  // styles for child component
}
```
Here, we are using a compound selector to target the specific instance of the <code>ChildComponent</code> with the <code>child1</code> class name.

---

**Me:**
that does not make any sense, parent and child stored in different modules as their styles. I simply cant use child classname, because if i import it from another module it will redefined with that module prefix

---

**ChatGPT:**
If your parent and child components are defined in different modules, and their class names are being modified by SCSS with module prefixes, you can still use the <code>displayName</code> property to target child components in your SCSS file.
To do this, you can define the <code>displayName</code> property on the child component itself, and then use that value to target the component in your SCSS file.
For example, let's say your child component is defined in <code>Child.js</code> with the <code>displayName</code> property set to <code>"ChildComponent"</code>, and your parent component is defined in <code>Parent.js</code> with styles in <code>Parent.module.scss</code>. You can target the child component in your SCSS file like this:
```scss
.Parent_ClassName:hover .ChildComponent {
  // styles for child component
}
```
Here, we are using the <code>displayName</code> property <code>"ChildComponent"</code> to target the child component inside the <code>Parent</code> component.
If the child component is defined with a different name in the module where it is imported, you can still use the <code>displayName</code> property to target it, as long as you are importing the component with its original name. For example, if the child component is defined in <code>Child.js</code> with a <code>displayName</code> of <code>"ChildComponent"</code>, and you are importing it into <code>Parent.js</code> with a different name like this:
```js
import DifferentName from './Child';
```
You can still use the <code>displayName</code> property to target the component like this:
```scss
.Parent_ClassName:hover .ChildComponent {
  // styles for child component
}
```
Here, we are using the original <code>displayName</code> value of <code>"ChildComponent"</code>, even though we are importing the component with a different name.

---

**Me:**
nonsence. Okay tell me the right way to style child component in parent scss module without giving it additional class in place 

---

**ChatGPT:**
To style a child component from a parent SCSS module without giving it an additional class, you can use the <code>&amp;</code> operator to refer to the parent component, and then target the child component using its tag name, class name, or <code>displayName</code>.
For example, if your parent component has a class name of <code>Parent</code>, and your child component has a <code>displayName</code> of <code>ChildComponent</code>, you can style the child component like this:
```scss
.Parent:hover {
  & ChildComponent {
    // styles for child component
  }
}
```
Here, we are using the <code>&amp;</code> operator to refer to the parent component, and then targeting the child component using its <code>displayName</code>.
If you don't want to use the <code>displayName</code>, you can target the child component using its tag name or class name like this:
```scss
.Parent:hover {
  & .child-class {
    // styles for child component with class name "child-class"
  }
  
  & div {
    // styles for child component with tag name "div"
  }
}
```
Here, we are using the <code>&amp;</code> operator to refer to the parent component, and then targeting the child component using its class name or tag name.

---

**Me:**
story with displayName not working for me. Do I miss any settings for react app, that makes it works? Also i use functional components, maybe thats the case?

---

**ChatGPT:**
The <code>displayName</code> property should work for functional components as well as class components. However, in order for the <code>displayName</code> to be visible in the React DevTools, you need to make sure that the <code>react-devtools-extended</code> browser extension is installed and enabled.
Once you have the extension installed and enabled, you should be able to see the <code>displayName</code> property in the React DevTools when inspecting your components.
If you are still having issues with the <code>displayName</code> property not working, make sure that you are setting it correctly in your child component. Here's an example of how to set the <code>displayName</code> property for a functional component:
```jsx
import React from 'react';

const ChildComponent = (props) => {
  // component logic here
};

ChildComponent.displayName = 'ChildComponent';

export default ChildComponent;
```
Make sure that you are setting the <code>displayName</code> property after you define the component, and that you are using the correct syntax for the property name (i.e. <code>displayName</code>, not <code>displayname</code>).

---

**Me:**
that thing with displayName compiles in .Parent:hover ChildComponent { ... }. Obviously in build version I wont have any ChildComponent tag. ChildComponent becomes a div with other inner content. So that does not work 

---

**ChatGPT:**
If the child component is being rendered as a <code>div</code> with other inner content, then you won't be able to target it using the <code>ChildComponent</code> tag name in your SCSS.
In that case, you will need to use a class or an attribute selector to target the child component. One way to do this is to add a class to the child component, and then target that class in your SCSS.
For example, in your child component:
```jsx
import React from 'react';
import styles from './ChildComponent.module.scss';

const ChildComponent = (props) => {
  return (
    <div className={styles.child}>
      {/* inner content */}
    </div>
  );
};

export default ChildComponent;
```
And then in your parent component SCSS:
```scss
.Parent {
  /* styles for parent component */

  &:hover {
    .child {
      /* styles for child component */
    }
  }
}
```
In this example, <code>styles.child</code> refers to a CSS class that you define in your <code>ChildComponent.module.scss</code> file, which can be imported and used in your child component. Then, in your parent component SCSS, you can use the <code>.child</code> class to target the child component using a descendant selector (<code> .Parent:hover .child</code>).

---

**Me:**
That doesnt work. What the best solution you can give me to solve this problem? Is that passing className through props?

---

**ChatGPT:**
If passing a class name as a prop to the child component is not an option, then you could use a class name or an attribute selector to target the child component in your SCSS.
One way to do this is to add a class to the child component, and then target that class in your SCSS. For example:
```jsx
import React from 'react';
import styles from './ChildComponent.module.scss';

const ChildComponent = (props) => {
  return (
    <div className={`${props.className} ${styles.child}`}>
      {/* inner content */}
    </div>
  );
};

export default ChildComponent;
```
In this example, we are using template literals to concatenate the <code>className</code> prop passed from the parent component with the <code>child</code> class defined in the <code>ChildComponent.module.scss</code> file.
Then, in your parent component SCSS, you can use the class name or attribute selector to target the child component using a descendant selector (<code> .Parent:hover .child</code>).
For example:
```scss
.Parent {
  /* styles for parent component */

  &:hover {
    .child {
      /* styles for child component */
    }
  }
}
```
Alternatively, if you want to use an attribute selector, you could add a custom data attribute to the child component, and then use the attribute selector to target it. For example:
```jsx
import React from 'react';
import styles from './ChildComponent.module.scss';

const ChildComponent = (props) => {
  return (
    <div data-child-component className={props.className}>
      {/* inner content */}
    </div>
  );
};

export default ChildComponent;
```
In this example, we have added a <code>data-child-component</code> attribute to the child component, which we can use to target it in our SCSS.
Then, in your parent component SCSS, you can use the attribute selector to target the child component using a descendant selector (<code> .Parent:hover [data-child-component]</code>).
For example:
```scss
.Parent {
  /* styles for parent component */

  &:hover {
    [data-child-component] {
      /* styles for child component */
    }
  }
}
```
I hope this helps! Let me know if you have any more questions.
