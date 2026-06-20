---
uuid: "20260620003538"
type: post
title: Test for Obsidian Bulk Tag Manager on version 1.4.0
author: codeshell
description:
date: 2026-06-19
published: 2026-06-19
created: 2026-06-19T16:01:00+02:00
lastmod: 2026-06-20T00:53:00+02:00
tags:
  - published-by-me
category: blog
parent:
share: true
slug: test-for-obsidian-bulk-tag-manager-on-version-140
---

## Overview

![](../../_assets/img/Pasted%20image%2020260618230108.png)

## Invalid Tags (Real-time)

![](../../_assets/img/Pasted%20image%2020260618230308.png)

> [!QUESTION]
> Any way to "view" what is deemed invalid prior to fixing?
> Because some "invalid" tags are expected as in this example: `tags: "{{VALUE:tags}}"`

> [!CHECK] Answer
> I would suggest renaming the button to "Preview and Fix" or "View invalid" or something to indicate to the user that nothing is executed just by clicking the red button.
>
> My personal preference for this button would be:
> - Label: "Manage invalid tags"
> - Color: Default Obsidian Purple

|        | Before Fix                                                                           | After Fix                                                                      |
| ------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| File 1 | `tags: "{{VALUE:tags}}"`                                                             | ignored                                                                        |
| File 2 | tags:<br>  - food<br>  - "#food/lunch"<br>  - "#food/takeaway"<br>  - region/vietnam | tags:<br>  - food<br>  - food/lunch<br>  - food/takeaway<br>  - region/vietnam |
| File 3 | tags:<br>  - "#🗑️"                                                                  | tags:<br>  - 🗑️                                                               |
| File 4 | tags:<br>  - "#🗑️"<br>  - service                                                   | tags:<br>  - 🗑️<br>  - service                                                |

![](../../_assets/img/Pasted%20image%2020260618232924.png)

> [!faq] Issue?
> It is not possible to use "excluded folders" or "protected tags" to safeguard templates with special tag variables.

![](../../_assets/img/Pasted%20image%2020260618231907.png)

![](../../_assets/img/Pasted%20image%2020260618231924.png)

> [!CHECK]
> Directly ignoring works. From `data.json`:
> ```unknown
>   "ignoredIssues": [    "_meta/templates/new-memo.md|Front matter tags \"{{VALUE:tags}}\" contains prohibited special characters"  ],
> ```

![](../../_assets/img/Pasted%20image%2020260618232908.png)

> [!faq] Issue?
> The "starts with #" and "special chars" rule produce duplicates.

> [!BUG]
> I tested by clicking "Update" on one of the dupes.
> That entry vanished.
> The second entry remains.

> [!IMPORTANT] Update
> I misunderstood "Update". It does not "Autofix" the invalid char. If you just click "Update", the entry is removed from the view but nothing in the note is fixed.
> Not a big deal, because nothing breaks.
>
> My suggestions:
> - "Update"-Button is disabled as long as the text field has not changed by the user.
> - Every tag must only be listed once. If one tag triggers multiple violations, they could be written together above the same text box.

![](../../_assets/img/Pasted%20image%2020260618235206.png)

![](../../_assets/img/Pasted%20image%2020260618235314.png)

![](../../_assets/img/Pasted%20image%2020260618235350.png)

> [!HINT] Enhancement
> It would be amazing to have the rules checked "onChange" so that the "Update"-Button stays disabled as long as the user puts something strange in.
> I broke it deliberately with my `{{am-i-valid?}}` tag, but I am sure some users will input and save wrong new tag names without realizing that they are invalid as well.

## Tag format style / wikilink format style

![](../../_assets/img/Pasted%20image%2020260619003151.png)

I don't understand the part about wiki links.

I use obsidian-linter to keep all properties of array type (=Obsidian property type "list") consistent as multi-line arrays (or YAML List, as you put it). Example from linter settings:

![](../../_assets/img/Pasted%20image%2020260619004824.png)

Indeed, "standardizing" the tags format makes sense for people who don't use a linter. The reason this works is because Obsidian requires (forces) the "tags" property to be a list / array.

But how do the "wiki links" from your Metadata Utilities fit in here? The decision to use inline vs multi-line arrays is only relevant for properties that have the List type:

![](../../_assets/img/Pasted%20image%2020260619005937.png)

If you change the format based on if the value of the property is a wiki link, you would end up with changing text properties to list properties (thus breaking them, when they are not "Automatic", but set to "Text"). Or you would end up with mixed property fields when the same property has a wiki link on one note (thus getting "arrayed") and a text or markdown link on another note (thus staying as text).

Again, I don't know what to expect from this one so I will just leave it at that. :)

## Rename tags

![](../../_assets/img/Pasted%20image%2020260619032742.png)

![](../../_assets/img/Pasted%20image%2020260619032756.png)

![](../../_assets/img/Pasted%20image%2020260619032808.png)

![](../../_assets/img/Pasted%20image%2020260619032817.png)

![](../../_assets/img/Pasted%20image%2020260619032833.png)

Only 4 notes changed, however, there where 87 changes:

![](../../_assets/img/Pasted%20image%2020260619033106.png)

4 files + 8 history + data.json. Remaining 75 are frontmatter "cleaning" changes.

For examples, see [another new tag](2026-06-19-test-for-obsidian-bulk-tag-manager-on-version-140.md##delete-tags)

> [!BUG] Issue
> It looks like "Rename Tags" triggers "Clean front matter formatting"?

The `data.json` contained:

```json
  "operationHistory": [
    {
      "id": "e7b9f5d4-700c-4281-a9ca-6db05f6b28c6",
      "timestamp": 1781832504154,
      "type": "rename",
      "description": "Batch rename: 4 pairs (4 files changed)",
      "changes": [],
      "useExternalStorage": true,
      "useExternalManifest": true
    }
  ],
```

> [!INFO] changes reverted

## Merge Tags

![](../../_assets/img/Pasted%20image%2020260619022331.png)

![](../../_assets/img/Pasted%20image%2020260619022357.png)

![](../../_assets/img/Pasted%20image%2020260619022723.png)

True. The `#books` tag only exists in my `_test` folder.

![](../../_assets/img/Pasted%20image%2020260619022942.png)

![](../../_assets/img/Pasted%20image%2020260619022954.png)

![](../../_assets/img/Pasted%20image%2020260619023010.png)

Only 10 books should be changed, however, there are 103 changed files:

![](../../_assets/img/Pasted%20image%2020260619023301.png)

10 books + 20 history files (before + after) + data.json are expected. The rest contains frontmatter cleaning.

For examples, see [another new tag](2026-06-19-test-for-obsidian-bulk-tag-manager-on-version-140.md##delete-tags)

> [!BUG] Issue
> It looks like "Merge Tags" triggers "Clean front matter formatting"?

The `data.json` contained:

```json
  "operationHistory": [
    {
      "id": "efacd254-d47e-418d-834c-6926f5ca8622",
      "timestamp": 1781829000024,
      "type": "merge",
      "description": "Merge #books, #📚Book → #book",
      "changes": [],
      "useExternalStorage": true,
      "useExternalManifest": true
    }
  ],
```

> [!INFO] changes reverted

## Nest Tags

![](../../_assets/img/Pasted%20image%2020260619031144.png)

> [!NOTE]
> The hashtag from status is indeed not visible when using "Search" to select the tag. Seems just a visual glitch.

![](../../_assets/img/Pasted%20image%2020260619031346.png)

![](../../_assets/img/Pasted%20image%2020260619031409.png)

![](../../_assets/img/Pasted%20image%2020260619031417.png)

![](../../_assets/img/Pasted%20image%2020260619031443.png)

177 files changed.

![](../../_assets/img/Pasted%20image%2020260619031744.png)

34 expected + 68 history + data.json.

The rest contains frontmatter cleaning.

For examples, see [another new tag](2026-06-19-test-for-obsidian-bulk-tag-manager-on-version-140.md##delete-tags)

> [!BUG] Issue
> It looks like "Nest Tags" triggers "Clean front matter formatting"?

The `data.json` contained:

```json
  "operationHistory": [
    {
      "id": "7ff05ee6-4a32-4bdb-b88f-ff641498d6dc",
      "timestamp": 1781831671614,
      "type": "nest",
      "description": "Nest #uninstalled, #active, #inactive, #running → #status/...",
      "changes": [],
      "useExternalStorage": true,
      "useExternalManifest": true
    }
  ],
```

> [!INFO] changes reverted

## Delete tags

![](../../_assets/img/Pasted%20image%2020260619015919.png)

Only one file should have changed:

![](../../_assets/img/Pasted%20image%2020260619020558.png)

However, there where 78 changed files:

![](../../_assets/img/Pasted%20image%2020260619020659.png)

`0.after` and `0.before` are the bulk-tag-manager history files, which is correct.

However, 75 unrelated files where changed: The reason: Quotation adjustments in the frontmatter:

Example 1:

![](../../_assets/img/Pasted%20image%2020260619020929.png)

Example 2:

![](../../_assets/img/Pasted%20image%2020260619021115.png)

> [!BUG] Issue
> It looks like "Delete Tags" triggers "Clean front matter formatting"?

The `data.json` contained:

```json
  "operationHistory": [
    {
      "id": "abb8eb50-4e63-40e0-aef9-3ac38a55cb57",
      "timestamp": 1781827074306,
      "type": "delete",
      "description": "Deleted tags: Colbert",
      "changes": [],
      "useExternalStorage": true,
      "useExternalManifest": true
    }
  ],
```

> [!INFO] changes reverted

## Delete Tags ("untag" unintended "tags")

When looking for tags to delete, I found that rather than deleting them, I might have to escape them instead when they are inline. The reason is that in my case they are false positives, identified by Obsidian as tags while they are just random text strings that happen to begin with a hash tag:

![](../../_assets/img/Pasted%20image%2020260619012801.png)

This is not a bug, just a reminder that users might break their text when they delete tags they don't recognize. In my case, I never added a `#N` tag but obviously the "iptables Tutorial" contains text that Obsidian interprets as tags.

For me, instead of deleting those "strange" tags, I search&replaced them into inline code.

Another more common example: Writing a note about Microsoft Excel formula errors like `#VALUE` or `#N/A` or '#REF' will create unintended tags if the user does not remember to escape them with code blocks.

## Pattern Rename

![](../../_assets/img/Pasted%20image%2020260619025328.png)

![](../../_assets/img/Pasted%20image%2020260619025349.png)

![](../../_assets/img/Pasted%20image%2020260619025406.png)

![](../../_assets/img/Pasted%20image%2020260619025441.png)

Only one note had a nested wip tag that had to be transformed.

There are 229 changes instead.

![](../../_assets/img/Pasted%20image%2020260619030335.png)

1 pattern match + 2 history files + 1 data.json. Then 75 frontmatter "fixes" + 150 history files.

> [!BUG] Issue
> It looks like "Regex rename" triggers "Clean front matter formatting" and also saves those files to history (unlike in the other cases)?

The `data.json` contained:

```json
  "operationHistory": [
    {
      "id": "c6e2d349-b46d-4265-a740-068e10e4436e",
      "timestamp": 1781830468102,
      "type": "pattern",
      "description": "Pattern: /^wip/(.*)$/ → todo/$1",
      "changes": [],
      "useExternalStorage": true,
      "useExternalManifest": true
    }
  ],
```

> [!INFO] changes reverted

## Aliases

![](../../_assets/img/Pasted%20image%2020260619024844.png)

Works for me.
