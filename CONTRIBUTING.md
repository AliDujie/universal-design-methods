# Contributing Guide / 贡献指南

Thank you for your interest in contributing to Universal Design Methods!
感谢你对通用设计方法技能的贡献！

## How to Contribute / 如何贡献

### 📚 Content Contributions / 内容贡献

- **Add new research methods**: Follow the existing method template in `references/` / 添加新的研究方法：遵循 references/ 中已有的方法模板
- **Improve method descriptions**: Clarify usage scenarios, prerequisites, or outputs / 改进方法描述：澄清使用场景、前提条件或产出
- **Add real-world examples**: Practical case studies for each method / 添加真实案例：为每种方法提供实践案例
- **Translate content**: Help make this skill accessible in more languages / 翻译内容：帮助本技能支持更多语言

### 🔧 Code Contributions / 代码贡献

- **Fix bugs**: Report and fix issues in the `udm/` module / 修复 bug：报告和修复 udm/ 模块中的问题
- **Add features**: New query capabilities, method comparison tools / 添加功能：新的查询能力、方法比较工具
- **Improve performance**: Optimize method search and filtering / 提升性能：优化方法搜索和过滤
- **Add tests**: Ensure reliability of the toolkit / 添加测试：确保工具包的可靠性

### 📝 Documentation / 文档贡献

- **Improve README**: Clearer instructions, better examples / 改进 README：更清晰的说明，更好的示例
- **Add tutorials**: Step-by-step guides for specific research scenarios / 添加教程：特定研究场景的分步指南
- **Update references**: Keep the 100 methods current and accurate / 更新参考文档：保持 100 种方法的准确性和时效性

## Development Setup / 开发环境

```bash
# Clone the repository
git clone https://github.com/AliDujie/universal-design-methods.git
cd universal-design-methods

# Install in development mode / 安装开发模式
pip install -e ".[dev]"

# Run tests / 运行测试
pytest

# Lint code / 代码检查
ruff check .
```

## Pull Request Process / PR 流程

1. Fork the repository / Fork 仓库
2. Create a feature branch (`git checkout -b feature/amazing-feature`) / 创建功能分支
3. Make your changes / 进行修改
4. Run tests and linting / 运行测试和代码检查
5. Commit with descriptive messages / 使用描述性的提交信息
6. Push to your fork and submit a PR / 推送到你的 Fork 并提交 PR

## Code Style / 代码规范

- Follow PEP 8 guidelines / 遵循 PEP 8 规范
- Use type hints for new code / 新代码使用类型标注
- Add docstrings for all public functions / 为所有公共函数添加文档字符串
- Keep line length under 100 characters / 行长度不超过 100 字符

## Related Skills / 相关技能

When contributing, consider how UDM fits into the broader AliDujie UX Research ecosystem:

- [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) — UDM 定性发现可输入 JTBD 分析
- [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) — UDM 定性发现用 QuantUX 定量验证
- [Web Persona](https://github.com/AliDujie/web-persona-skill) — UDM 合成阶段产出可构建 Persona
- [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) — UDM 生成阶段方法可与 VPD 结合
- [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) — UDM 研究报告可交给 SWD 进行数据叙事

---

*By contributing, you agree that your contributions will be licensed under the MIT License.*
*通过贡献，你同意你的贡献将在 MIT 许可下授权。*
