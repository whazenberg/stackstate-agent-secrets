from stackstate_checks.base import AgentCheck

__version__ = "1.0.0"

class HelloCheck(AgentCheck):
    def check(self, instance):
        self.log.info(instance)
