package bytevector;

import org.junit.jupiter.api.Test;
import static org.junit.Assert.assertEquals;

public class XClassTest {
    @Test
    public void test_get() {
        XClass x = new XClass(0);
        assertEquals(0, x.getValue());
    }
}
