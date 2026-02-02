# ServiceProvider

Returns a service with the class name requested. When called with the name of a service it will return the instance of that service. If the service does not yet exist it will be created and the new service is returned.

### Code Samples <a href="#code-samples" id="code-samples"></a>

#### ServiceProvider:GetService <a href="#serviceprovider-getservice" id="serviceprovider-getservice"></a>

```lua
local UserInputService = game:GetService("UserInputService")
```

### Parameters <a href="#parameters" id="parameters"></a>

| Name                              | Type   | Default | Description                             |
| --------------------------------- | ------ | ------- | --------------------------------------- |
| <h4 id="classname">className</h4> | string |         | The class name of the requested service |

### Returns <a href="#returns" id="returns"></a>

| Return Type                     | Summary                              |
| ------------------------------- | ------------------------------------ |
| <h4 id="instance">Instance</h4> | An instance of the requested service |
