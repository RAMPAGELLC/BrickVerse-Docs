# Porting your Roblox Place (.rbxl/.rbxlx) to BrickVerse

## Converting a Roblox World to BrickVerse

`RBLX2BRICKWORLD` is a migration tool for converting a Roblox place into a BrickVerse World file. It reads the Roblox place hierarchy, converts supported objects into their closest BrickVerse equivalents, and can optionally pass scripts to the Roblox Luau-to-BrickLua translator.

{% hint style="danger" %}
World conversion is not guaranteed to reproduce a Roblox experience exactly. Always import the converted World into BrickVerse Creator and review its objects, properties, scripts, lighting, collisions, and gameplay behavior.
{% endhint %}

### What the converter supports

The converter is primarily intended for transferring map content from Roblox `Workspace`.

Currently supported object categories include:

| Roblox content     | Conversion status                         |
| ------------------ | ----------------------------------------- |
| `Part`             | Supported                                 |
| `MeshPart`         | Supported                                 |
| Models and folders | Supported where represented by the parser |
| Lights             | Supported                                 |
| Scripts            | Supported through `RBLXLuau2BrickLua`     |
| Terrain            | Not currently supported                   |

The supported-class list is still being expanded.

{% hint style="danger" %}
Roblox Terrain is not currently converted. Terrain data may be skipped, represented as migration metadata, or require manual rebuilding in BrickVerse Creator.
{% endhint %}

### Requirements

Install the following before using the converter:

* [Node.js](https://nodejs.org/)
* [TypeScript](https://www.typescriptlang.org/)
* [RBLX2BRICKWORLD](https://github.com/BrickVerse-co/RBLX2BRICKWORLD)
* [RBLXLuau2BrickLua](https://github.com/BrickVerse-co/RBLXLuau2BrickLua)
* [rbxlxparser](https://github.com/RAMPAGELLC/rbxlxparser)

The script translator is required when script conversion is enabled.

### Prepare your Roblox place

Before exporting your place, create a backup in Roblox Studio.

For the cleanest result:

1. Move the map content you want to convert under `Workspace`.
2. Remove test objects, temporary models, and unused scripts.
3. Apply transforms to important Parts and MeshParts.
4. Check that important Parts have the correct `Anchored` and `CanCollide` values.
5. Replace unsupported or proprietary Roblox objects where possible.
6. Save the place as an `.rbxlx` file when XML input is supported by your build.

An `.rbxlx` file is generally easier to inspect and process because it stores the place as XML.

{% hint style="info" %}
The converter uses `rbxlxparser` to read Roblox XML place data. Binary `.rbxl` support depends on the parser and converter version being used.
{% endhint %}

### Install the converter

Clone the converter repository:

```bash
git clone https://github.com/BrickVerse-co/RBLX2BRICKWORLD.git
cd RBLX2BRICKWORLD
```

Install the project dependencies using the package command supplied by the repository:

```bash
npm install
```

If the project requires a TypeScript build, compile it using the script defined in its `package.json`:

```bash
npm run build
```

{% hint style="warning" %}
The repository README may define a different build or execution command as the project develops. Use the command documented by the version you downloaded.
{% endhint %}

### Convert a place

The converter needs:

* an input `.rbxl` or `.rbxlx` place;
* an output path;
* and any optional migration settings.

The general command structure is:

```bash
<converter-command> <input-place> <output-world>
```

For example:

```bash
<converter-command> "./places/MyRobloxPlace.rbxlx" "./output/MyBrickVerseWorld.world"
```

Replace `<converter-command>` with the executable, npm script, or TypeScript entry point provided by the repository.

Some versions may use `.brickworld`, `.bvxw`, or `.world` as the output extension. Use the extension supported by your current BrickVerse Creator build.

### Convert scripts with the World

When script conversion is enabled, the World converter sends Roblox scripts to `RBLXLuau2BrickLua`.

A typical conversion flow is:

```
Roblox place
    ├── Workspace objects
    ├── Parts and MeshParts
    ├── Lights
    └── Scripts
            ↓
RBLX2BRICKWORLD
    ├── Converts World objects
    └── Sends scripts to RBLXLuau2BrickLua
            ↓
BrickVerse World file
```

Enable script conversion only when the script translator is installed and accessible to the World converter.

{% hint style="warning" %}
Translated scripts are migration drafts. They must be reviewed before the converted World is published.
{% endhint %}

### Recommended conversion workflow

Do not begin by converting the production copy of a large experience.

Start with a small test:

1. Create a Roblox place containing a few Parts, a Model, a light, and one simple script.
2. Export it as `.rbxlx`.
3. Convert it to a BrickVerse World.
4. Open the output in BrickVerse Creator.
5. Compare the converted hierarchy with the original place.
6. Correct the conversion configuration as needed.
7. Convert the full place only after the test succeeds.

### Open the converted World

After conversion:

1. Open BrickVerse Creator.
2. Open or import the generated World file.
3. Allow Creator to load the converted hierarchy.
4. Check the output and error console.
5. Save the World as a new BrickVerse project before making large changes.

Keep the original Roblox place and generated conversion report until migration is complete.

### Review the hierarchy

Compare the BrickVerse hierarchy with the original Roblox `Workspace`.

Check for:

* missing Models;
* flattened folders;
* incorrectly parented objects;
* unsupported classes;
* duplicate object names;
* missing scripts;
* and objects placed outside the expected World hierarchy.

Objects with no direct BrickVerse equivalent may be skipped or replaced with placeholders.

### Review Part properties

Inspect important Parts and MeshParts for:

* position;
* rotation;
* size;
* color;
* material;
* transparency;
* anchoring;
* collision;
* shadows;
* and mesh appearance.

Coordinate systems and rotation formats can differ between engines. Large or rotated Models should be checked carefully.

### Review lighting

Check converted lights for:

* light type;
* enabled state;
* range;
* intensity;
* color;
* shadows;
* and parent object.

Global Roblox lighting settings may not have a direct one-to-one BrickVerse equivalent.

### Review MeshParts and assets

A MeshPart may require its mesh and texture assets to be available to BrickVerse.

The converter may preserve an asset identifier without automatically uploading the source asset.

After import:

1. Check whether the mesh appears.
2. Replace inaccessible Roblox asset references.
3. Upload assets you own through BrickVerse.
4. Assign the resulting BrickVerse assets.
5. Verify scale and collision.

{% hint style="danger" %}
Only migrate assets that you created, own, or have permission to use. Converting an asset reference does not grant permission to republish the asset.
{% endhint %}

### Terrain

Roblox Terrain is currently unsupported by the public converter documentation.

Terrain must generally be:

* rebuilt manually in BrickVerse Creator;
* converted through a future Terrain-specific importer;
* or approximated using Parts and meshes before conversion.

For map migrations where Terrain is important, convert the structural map first and rebuild Terrain around the imported geometry.

### Review converted scripts

For every converted script:

1. Open it in the BrickVerse script editor.
2. Read translator warnings.
3. Find remaining Roblox class and service names.
4. verify whether it should run on the server or client.
5. Replace unsupported API calls.
6. Reconnect networking.
7. Test datastore behavior.
8. Validate all client requests on the server.

Search converted scripts for common Roblox-only terms:

```
workspace
ReplicatedStorage
ServerStorage
ServerScriptService
StarterGui
RemoteEvent
RemoteFunction
CFrame
TweenService
CollectionService
DataStoreService
Humanoid
```

Their presence does not always indicate an error, but each occurrence should be reviewed.

### Test the converted World

Test the World in this order:

#### Static map test

Check:

* object placement;
* scale;
* materials;
* lighting;
* collision;
* and missing assets.

#### Script test

Check:

* script startup errors;
* missing services;
* unsupported methods;
* event connections;
* and client/server placement.

#### Multiplayer test

Check:

* replication;
* player spawning;
* network events;
* server authority;
* damage validation;
* and persistent data.

#### Performance test

Check:

* excessive Part counts;
* unnecessary collision;
* large meshes;
* repeated script loops;
* and excessive network messages.

### Troubleshooting

#### The converter cannot read the file

Confirm that:

* the file exists;
* it is a supported `.rbxl` or `.rbxlx` format;
* it is not corrupted;
* and the required parser is installed.

Try exporting the place as `.rbxlx` from Roblox Studio.

#### Terrain is missing

Terrain is not currently supported. Rebuild it in BrickVerse Creator or replace it with convertible geometry before migration.

#### Parts are rotated incorrectly

Check the converter's coordinate and rotation options. Complex Roblox `CFrame` values may require conversion into BrickVerse position and rotation properties.

#### Meshes are invisible

The original asset may not be accessible to BrickVerse. Upload an authorized copy and assign the new asset.

#### Scripts still use Roblox APIs

Run the script translator, then manually review anything it could not map safely.

#### The generated World does not open

Confirm that the output extension and format are supported by your BrickVerse Creator version. Review the converter console and migration report for serialization errors.

### Limitations

The converter should be treated as a migration assistant rather than a complete compatibility layer.

Some systems normally require manual rebuilding:

* Roblox Terrain;
* RemoteEvents and RemoteFunctions;
* constraints;
* advanced physics;
* CFrame-heavy systems;
* TweenService animations;
* Roblox-specific UI layouts;
* MarketplaceService;
* DataStoreService architecture;
* PathfindingService;
* and platform-specific character behavior.

### Related tools

* [RBLX2BRICKWORLD](https://github.com/BrickVerse-co/RBLX2BRICKWORLD)
* [RBLXLuau2BrickLua](https://github.com/BrickVerse-co/RBLXLuau2BrickLua)
* [rbxlxparser](https://github.com/RAMPAGELLC/rbxlxparser)
* [BrickVerse Game API](https://developers.brickverse.gg/game-api/api)
