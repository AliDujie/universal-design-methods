# UDM Runnable Examples / 可运行示例

These examples demonstrate Universal Design Methods capabilities with real-world scenarios.
这些示例用真实场景演示通用设计研究方法能力。

## Quick Start / 快速开始

```bash
cd examples/
python 01_method_recommend.py
```

All examples use **zero dependencies** — pure Python standard library only.
所有示例使用**零依赖** — 仅 Python 标准库。

## Available Examples / 可用示例

### 01_method_recommend.py
Research method recommendation for a given research goal and phase.
根据研究目标和阶段推荐研究方法。

**Use when / 适用场景**: You need to select the right research method(s) for a project.

```bash
python 01_method_recommend.py
```

### 02_usability_test.py
Usability test script generation with SUS scoring.
生成可用性测试脚本并计算 SUS 分数。

**Use when / 适用场景**: Planning a usability test or evaluating an existing one.

```bash
python 02_usability_test.py
```

### 03_interview_guide.py
Interview guide generation with structured question types.
生成结构化访谈提纲。

**Use when / 适用场景**: Preparing for user interviews with specific research goals.

```bash
python 03_interview_guide.py
```

## Tips / 提示

- All examples use relative imports — just run from the `examples/` directory
- No `pip install` required — UDM is zero-dependency
- Combine with SWD examples for research report visualization
- See [USAGE.md](../USAGE.md) for detailed API documentation
