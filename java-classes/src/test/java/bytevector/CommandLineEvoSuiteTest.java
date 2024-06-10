
package bytevector;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class CommandLineEvoSuiteTest {

  @Test
  public void test0() throws Throwable {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add(">P'Y", ">P'Y");
      assertEquals(true, boolean0);
  }

  @Test
  public void test1() throws Throwable {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.isParameter("-");
      assertEquals(false, boolean0);
  }

  @Test
  public void test2() throws Throwable {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.isSwitch("!o*u");
      assertEquals(false, boolean0);
  }

  @Test
  public void test3() throws Throwable {
      String[] stringArray0 = new String[8];
      stringArray0[0] = "-";
      stringArray0[1] = "-";
      stringArray0[2] = "";
      stringArray0[3] = "-";
      stringArray0[4] = "-";
      stringArray0[5] = "-";
      stringArray0[6] = "";
      stringArray0[7] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      assertNotNull(commandLine0);
      
      boolean boolean0 = commandLine0.exists("");
      assertEquals(true, boolean0);
  }

  @Test
  public void test4() throws Throwable {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.exists(">P'Y");
      assertEquals(false, boolean0);
  }

  @Test
  public void test5() throws Throwable {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.isSwitch("TestSwitch");
      assertEquals(false, boolean0);
  }

  @Test
  public void test6() throws Throwable {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.isParameter("Param1");
      assertEquals(false, boolean0);
  }

  @Test
  public void test7() throws Throwable {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("Option1", "Value1");
      assertEquals(true, boolean0);
  }

  @Test
  public void test8() throws Throwable {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("Option1", "Value1", false);
      assertEquals(true, boolean0);
  }

  @Test
  public void test9() throws Throwable {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("Option1", null);
      assertEquals(true, boolean0);
  }

  @Test
  public void test10() throws Throwable {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.exists("Option1");
      assertEquals(false, boolean0);
  }

  @Test
  public void test11() throws Throwable {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.isParameter("Param2");
      assertEquals(false, boolean0);
  }

  @Test
  public void test12() throws Throwable {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.isSwitch("Switch1");
      assertEquals(false, boolean0);
  }

  @Test
  public void test13() throws Throwable {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.isSwitch("Switch2");
      assertEquals(false, boolean0);
  }

  @Test
  public void test14() {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("Key1", "Value1");
      assertEquals(true, boolean0);
      
      boolean boolean1 = commandLine0.add("Key1", "Value2", false);
      assertEquals(false, boolean1);
  }

}